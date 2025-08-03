import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, send_file, flash
from playwright.sync_api import sync_playwright
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'supersecret')

DB_PATH = "ecourt_queries.db"

# DB setup
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS queries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ts TIMESTAMP,
        case_type TEXT,
        case_number TEXT,
        filing_year TEXT,
        raw_response TEXT
    )''')
    conn.commit()
    conn.close()

init_db()

# Playwright Scraping
def fetch_case_details(case_type, case_number, filing_year):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # open search page
        page.goto("https://services.ecourts.gov.in/ecourtindia_v6/?p=casestatus/index&court_code=HRFBD", timeout=60000)
        # fill form
        page.select_option('select[name="case_type"]', case_type)
        page.fill('input[name="case_number"]', case_number)
        page.fill('input[name="case_year"]', filing_year)
        page.click('button:has-text("Search")')
        page.wait_for_load_state("networkidle")
        # scrape relevant details
        content = page.content()
        parties = page.inner_text('.party-names-selector')  # adjust selector as needed
        filing_date = page.inner_text('.filing-date-selector')
        next_hearing = page.inner_text('.next-hearing-selector')
        order_url = page.get_attribute('a.order-link-selector', 'href')
        browser.close()
    return {
        "parties": parties,
        "filing_date": filing_date,
        "next_hearing": next_hearing,
        "order_url": order_url,
        "raw": content
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        filing_year = request.form['filing_year']
        try:
            data = fetch_case_details(case_type, case_number, filing_year)
            # log to SQLite
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute('''INSERT INTO queries (ts, case_type, case_number, filing_year, raw_response)
                        VALUES (?, ?, ?, ?, ?)''',
                        (datetime.now(), case_type, case_number, filing_year, data['raw']))
            conn.commit()
            conn.close()
            return render_template('result.html', d=data)
        except Exception as e:
            flash(f"Error fetching case: {str(e)}")
    return render_template('index.html')

@app.route('/download')
def download():
    url = request.args.get('url')
    # Download PDF file (sanitize url etc.)
    ...

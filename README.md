Court-Data Fetcher & Mini-Dashboard
Overview
A simple web app to fetch and display Indian court case data by case type, number, and year. This mini-dashboard allows users to search for a case, view its details, and download the latest order/judgment PDFs.

Court Chosen
Example:

Delhi High Court (https://delhihighcourt.nic.in/)

(Replace with your chosen court and its URL if different, and explain why if relevant.)

Features
Simple UI for searching cases by Case Type, Case Number, and Filing Year.

Programmatic data fetch from the chosen court website.

Displays party names, filing date, next hearing date, and links to order/judgment PDFs.

Logs each search query and raw court data in a database.

User-friendly error messages for bad case numbers or court downtime.

Download feature for linked PDFs.

Tech Stack
Backend: Python (FastAPI/Flask/Scrapy/Requests/BeautifulSoup/Selenium/Playwright, etc.)

Frontend: HTML (Jinja2) / Bootstrap / React (if used, specify)

Database: SQLite or PostgreSQL (Specify your choice)

Other: Docker (optional), pytest/unittest (optional)

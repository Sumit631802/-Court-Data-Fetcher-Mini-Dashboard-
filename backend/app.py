from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# db = SQLAlchemy(app)

# from routes import user_routes
# app.register_blueprint(user_routes.bp)

# if __name__ == "__main__":
#     app.run(debug=True)
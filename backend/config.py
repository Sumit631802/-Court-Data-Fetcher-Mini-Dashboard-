import os

class Config:
    # PostgreSQL connection parameters (read from env vars or default here)
    DB_NAME = os.getenv('DB_NAME', 'your_db_name')
    DB_USER = os.getenv('DB_USER', 'your_db_user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'your_db_password')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')

    @classmethod
    def get_db_params(cls):
        return {
            'dbname': cls.DB_NAME,
            'user': cls.DB_USER,
            'password': cls.DB_PASSWORD,
            'host': cls.DB_HOST,
            'port': cls.DB_PORT,
        }

# Example usage:
# from config import Config
# conn = psycopg2.connect(**Config.get_db_params())

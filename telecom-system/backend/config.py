import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Default to MySQL, fallback to SQLite if not specified
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI", 
        "mysql+pymysql://root:password@localhost:3306/telecom_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

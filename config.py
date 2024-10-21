from dotenv import load_dotenv
import os


load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key')  # Replace with a secure key
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///artgallery.db')  # Fallback to SQLite for local dev
    SQLALCHEMY_TRACK_MODIFICATIONS = False

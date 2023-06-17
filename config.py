import os

from dotenv import load_dotenv


class Config:
    load_dotenv('.env')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = os.environ.get('SECRET_KEY')

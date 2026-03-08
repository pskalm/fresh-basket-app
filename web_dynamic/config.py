#!/usr/bin/python3
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('APP_SECRET_KEY')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = os.environ.get('DB_DATABASE')

db_config = {
    'host': '127.0.0.1',
    'user': DB_USER,
    'password': DB_PASSWORD,
    'database': DB_DATABASE,
    'use_pure': True
}
import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PWD = os.getenv("DATABASE_PWD")
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DJANGO_SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
DJANGO_DEBUG = os.getenv('DJANGO_DEBUG')
API_TOKEN = os.getenv('API_TOKEN')

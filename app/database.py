import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

conn = psycopg2.connect(os.getenv("DATABASE_URL"))

cursor = conn.cursor()

print("Database Connected Successfully!")
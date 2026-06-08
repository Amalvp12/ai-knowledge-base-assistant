import psycopg2

conn = psycopg2.connect(
    "postgresql://neondb_owner:npg_rhRaLS9w8vlx@ep-dark-wave-aqgp65il.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

cursor = conn.cursor()

print("Database Connected Successfully!")
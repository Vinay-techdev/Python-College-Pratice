import psycopg2
from sqlalchemy import create_engine, text

DATABASE_URL = (
    "postgresql://neondb_owner:npg_0jXH1NPcGZIR@ep-empty-bread-ah25040n-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

#? connection
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        print("Connection successful")
except Exception as e:
    print("Connection failed", e)

#? Create table
with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS public.students (
            std_id SERIAL PRIMARY KEY,
            name VARCHAR(10),
            grade CHAR
        )
    """))

print("Table created successfully")

#? Insert into table

with engine.begin() as conn:
    conn.execute(
        text("""
            INSERT INTO public.students (name, grade)
            VALUES 
             ('virat', ''A),
             ('ABD', 'A')
            """)
    )

print("Data inserted successfully")
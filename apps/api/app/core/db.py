import os
import psycopg


def get_db_connection():
    db_url = os.getenv("SUPABASE_DB_URL")
    if not db_url:
        raise RuntimeError("SUPABASE_DB_URL not set")

    return psycopg.connect(db_url)
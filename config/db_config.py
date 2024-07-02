# config/db_config.py
import psycopg2
from psycopg2 import sql

def get_db_connection():
    return psycopg2.connect(
        dbname="data_collection_db",
        user="postgres",
        password="postgress",
        host="localhost",
        port="5432"
    )

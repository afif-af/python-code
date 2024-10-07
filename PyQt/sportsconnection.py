# sportsconnection.py
import sqlite3

def connect_to_db(db_name):
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(db_name)
    return conn

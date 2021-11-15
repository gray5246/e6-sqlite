import sqlite3


def create_database():
    with sqlite3.connect('data/cafe.sqlite3') as s3:
        s3.execute("""CREATE TABLE IF NOT EXISTS stores (
       id INTEGER PRIMARY KEY,
       name  TEXT NOT NULL,
       type TEXT,
       cost_lb REAL)""")
        s3.execute("""CREATE TABLE IF NOT EXISTS coffees (
               id INTEGER PRIMARY KEY,
               name  TEXT NOT NULL,
               type TEXT,
               cost_lb REAL)""")
        s3.execute("""CREATE TABLE IF NOT EXISTS ratings (
               id INTEGER PRIMARY KEY,
               name  TEXT NOT NULL,
               type TEXT,
               cost_lb REAL)""")
        s3.execute("""CREATE TABLE IF NOT EXISTS specials (
               id INTEGER PRIMARY KEY,
               name  TEXT NOT NULL,
               type TEXT,
               cost_lb REAL)""")


def load_cafe_data():

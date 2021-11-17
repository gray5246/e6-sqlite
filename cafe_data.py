import sqlite3
import a3_examine

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
    coffee = a3_examine.dicter("coffees.csv")
    ratings = a3_examine.dicter("ratings.csv")
    specials = a3_examine.dicter("specials.csv")
    stores = a3_examine.dicter("stores.csv")
    coffee.remove(0)
    ratings.remove(0)
    specials.remove(0)
    stores.remove(0)
    with sqlite3.connect('data/cafe.sqlite3') as s3:
        for n, t, cl in coffee:
            s3.execute("INSERT INTO coffees (name, type, cost_lb", (n, t, int(cl)))
        for n, t, cl in ratings:
            s3.execute("INSERT INTO ratings (name, type, cost_lb", (n, t, int(cl)))
        for n, t, cl in specials:
            s3.execute("INSERT INTO specials (name, type, cost_lb", (n, t, int(cl)))
        for n, t, cl in stores:
            s3.execute("INSERT INTO stores (name, type, cost_lb", (n, t, int(cl)))
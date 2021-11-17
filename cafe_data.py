import sqlite3
import a3_examine


def create_database():
    with sqlite3.connect('data/cafe.sqlite3') as s3:
        s3.execute("""CREATE TABLE IF NOT EXISTS stores (
       id INTEGER PRIMARY KEY,
       name  TEXT NOT NULL,
       kind TEXT,
       volume REAL)""")
        s3.execute("""CREATE TABLE IF NOT EXISTS coffees (
               id INTEGER PRIMARY KEY,
               name  TEXT NOT NULL,
               type TEXT,
               cost_lb REAL)""")
        s3.execute("""CREATE TABLE IF NOT EXISTS ratings (
               id INTEGER PRIMARY KEY,
               date  TEXT NOT NULL,
               store_name TEXT,
               rating REAL)""")
        s3.execute("""CREATE TABLE IF NOT EXISTS specials (
               id INTEGER PRIMARY KEY,
               date  TEXT NOT NULL,
               store_name TEXT,
               coffee_name TEXT,
                price REAL)""")


def load_cafe_data():
    coffee = a3_examine.dicter("coffees.csv")
    ratings = a3_examine.dicter("ratings.csv")
    specials = a3_examine.dicter("specials.csv")
    stores = a3_examine.dicter("stores.csv")
    coffee.remove(coffee[0])
    ratings.remove(ratings[0])
    specials.remove(specials[0])
    stores.remove(stores[0])
    with sqlite3.connect('data/cafe.sqlite3') as s3:
        for n, t, cl in coffee:
            s3.execute("INSERT INTO coffees (name, type, cost_lb) VALUES (?, ?, ?)", (n, t, cl))
        for d, sn, r in ratings:
            s3.execute("INSERT INTO ratings (date, store_name, rating) VALUES (?, ?, ?)", (d, sn, r))
        for d, sn, cn, p in specials:
            s3.execute("INSERT INTO specials (date, store_name, coffee_name, price) VALUES (?, ?, ?, ?)", (d, sn, cn, p))
        for n, t, cl in stores:
            s3.execute("INSERT INTO stores (name, kind, volume) VALUES (?, ?, ?)", (n, t, cl))
def get_stores():
    with sqlite3.connect('data/cafe.sqlite3') as s3:
        result = s3.execute("select name,kind,volume from stores")

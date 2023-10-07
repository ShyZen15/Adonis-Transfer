import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS userdata(
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(25) NOT NULL
)
""")

username1, password1 = "admin", hashlib.sha256("root".encode()).hexdigest()
username2, password2 = "Shiven", hashlib.sha256("root".encode()).hexdigest()
username3, password3 = "Sarthak", hashlib.sha256("root".encode()).hexdigest()
username4, password4 = "Mritunjay", hashlib.sha256("root".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()
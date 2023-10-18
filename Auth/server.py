import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 1230))

server.listen()


def handle_connection(c):
    choice = c.recv(1024).decode()
    if choice == "L" or choice == "l":
        username = c.recv(1024).decode('utf-8')
        password = c.recv(1024).decode('utf-8')
        conn = sqlite3.connect("userdata.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))

        if cur.fetchall():
            c.send("True".encode())
            client.close()
        else:
            c.send("False".encode())
            client.close()

    elif choice == "Y" or choice == "y":
        conn = sqlite3.connect("userdata.db")
        cur = conn.cursor()

        c.send("Username: ".encode())
        username1 = c.recv(1024).decode()
        c.send("Password: ".encode())
        password1 = c.recv(1024)
        cur.execute(
            "SELECT * FROM userdata WHERE username = :username", dict(username=username1))
        if cur.fetchall():
            c.send("Taken".encode())
            client.close()

        else:

            cur.execute("""
                CREATE TABLE IF NOT EXISTS userdata(
                    id INTEGER PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    password VARCHAR(25) NOT NULL
                )
            """)

            cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
            conn.commit()

            c.send("Account Created!".encode())
            client.close()

    else:
        c.send("INVALID OPTION!".encode())
        raise SystemExit


while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()

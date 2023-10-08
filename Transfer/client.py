import os
import socket
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

key = get_random_bytes(16)
nonce = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_EAX, nonce)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

file = input("Enter the filename with extension: ")

file_tup = os.path.splitext(file)

file_ext = file_tup[1]

file_size = os.path.getsize(file)

with open(file, "rb") as f:
    data = f.read()

encrypted = cipher.encrypt(data)


client.send(file.encode())
client.send(str(file_ext).encode())
client.send(str(file_size).encode())
client.sendall(encrypted)
client.send(b"<END>")

client.close()

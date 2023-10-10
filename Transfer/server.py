import socket

# Define the hostname or IP address and the port number
server_host = '0.0.0.0'
server_port = 1234

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the hostname and port number
server_socket.bind((server_host, server_port))

total = int(input("Enter total number of clients: "))

# Start listening for incoming connections
server_socket.listen(total)

print('Server is listening for incoming connections...')

connections = []
for i in range(total):
    conn = server_socket.accept()
    connections.append(conn)
    print(f"Connected with client {i+1} with IP: {conn}")

# Accept an incoming connection
connection, client_address = server_socket.accept()

print('Connection established from', client_address)

# Receive the client's message
data = connection.recv(1024)

# Print the client's message
print('Received from client:', data.decode())

# Send a response to the client
message = 'Hello, Client!'
connection.sendall(message.encode())

# Close the connection
connection.close()
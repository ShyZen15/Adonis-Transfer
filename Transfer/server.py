import socket

# Define the hostname or IP address and the port number
server_host = '0.0.0.0'
server_port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the hostname and port number
server_socket.bind((server_host, server_port))

# Start listening for incoming connections
server_socket.listen(1)

print('Server is listening for incoming connections...')

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
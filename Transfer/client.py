import socket

# Define the server's hostname or IP address and the port number
server_host = '192.168.1.100' # Replace with your server's IP address
server_port = 1234

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))

# Send a message to the server
message = 'Hello, Server!'
client_socket.sendall(message.encode())

# Receive the server's response
data = client_socket.recv(1024)

# Print the server's response
print('Received from server:', data.decode())

# Close the socket
client_socket.close()

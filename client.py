import socket

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((host, port))

    while True:
        filename = input("Enter the name of the file you want to transfer: ")
        try:
            fi = open(filename, "r")
            data = fi.read()
            if not data:
                break
            while data:
                sock.send(str(data).encode())
                data = fi.read()
            
            fi.close()

        except IOError:
            print("You have enter invalid filename. Please enter a valid name")
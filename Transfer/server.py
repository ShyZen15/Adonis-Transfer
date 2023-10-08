import socket

import tqdm
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

hostname = socket.gethostname()

key = get_random_bytes(16)
nonce = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_EAX, nonce)


if __name__ == '__main__':
    # Defining Socket
    host = "localhost"
    print(host)
    port = 9999
    totalclient = int(input('Enter number of clients: '))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(totalclient)

    # Establishing Connections
    connections = []
    print('Initiating clients')
    for i in range(totalclient):
        conn = sock.accept()
        connections.append(conn)
        print('Connected with client ', i + 1)

    fileno = 0
    idx = 0
    for conn in connections:
        # Receiving File Data
        idx += 1
        data = conn[0].recv(1024).decode()

        if not data:
            continue

        print('Receiving file from client: ', idx)

        file_name = sock.recv(1024).decode()
        file_ext = sock.recv(1024).decode()
        file_size = sock.recv(1024).decode()
        # Creating a new file at server end and writing the data
        file = file_name + str(fileno) + file_ext
        fileno = fileno + 1
        fo = open(file, "wb")

        done = False

        file_bytes = b""

        progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))

        while not done:
            data = sock.recv(1024)
            if file_bytes[-5] == b"<END>":
                done = True
            else:
                file_bytes += data

            progress.update(1024)
        fo.write(cipher.decrypt(file_bytes[:-5]))

        print('Received successfully! New filename is: ', file)
        fo.close()
        sock.close()
    # Closing all Connections
    for conn in connections:
        conn[0].close()

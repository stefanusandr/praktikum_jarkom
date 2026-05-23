from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind ke port 6789 dan mulai listening
serverSocket.bind(('', 6790))
serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # Kirim header HTTP 200 OK
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Kirim isi file ke klien
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        # File tidak ditemukan → kirim 404
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>".encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()
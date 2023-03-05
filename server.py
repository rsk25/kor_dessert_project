import socket

# Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket object
s.bind((socket.gethostname(), 1234))

# make the server listen to client requests
s.listen(5)

while True:
    # contain client obj & address of client
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    # send info to client socket
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
    

    
import socket

# Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client needs to connect to server
s.connect((socket.gethostname(), 1234))

# receive message
msg = s.recv(1024) # buffer
print(msg.decode("utf-8"))

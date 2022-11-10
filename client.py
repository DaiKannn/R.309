import socket

# hope =True
# while hope =True :

message="hello."
client_socket = socket.socket()
client_socket.connect(("10.128.7.18", 10000))
client_socket.send(message.encode())
data = client_socket.recv(1024).decode()
print(message)
if message == "bye" :
    client_socket.close()

import socket

# hope = True
#
# while hope == True :
reply="moi avoir recu message"
server_socket = socket.socket()
server_socket.bind(("10.128.7.18", 10000))
server_socket.listen(1)
conn, address = server_socket.accept()
data = conn.recv(1024).decode()
conn.send(reply.encode())
print(reply)
conn.close()

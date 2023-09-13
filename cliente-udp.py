from socket import socket, AF_INET, SOCK_DGRAM


server_name = 'localhost'
server_port = 12000

client_socket = socket(AF_INET, SOCK_DGRAM)

msg= input("Entre minusculas \n")

client_socket.sendto(msg.encode(), (server_name,server_port))

msg_odificada, server_address = client_socket.recvfrom(2048)

print(msg_modificada.decode())
client_socket.close()
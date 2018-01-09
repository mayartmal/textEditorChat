import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('192.168.1.4', 5555))
print("server ok")

clients = []

while True:
    data, addr = server_socket.recvfrom(1024)

    if addr not in clients:
        clients.append(addr)

    #обработка

    print(data.decode('utf-8'))
    for client in clients:
        server_socket.sendto(data, client)

server_socket.close()

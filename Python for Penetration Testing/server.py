import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

server_socket.bind((host, port))

server_socket.listen(3)

while True:
    client_socket, addr = server_socket.accept()
    print(f"Received connection from {str(addr)}")
    msg = 'Thank you for connecting' + "\r\n"
    
    client_socket.send(msg.encode('ascii'))
    client_socket.close()
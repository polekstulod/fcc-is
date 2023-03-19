import socket


def banner(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    s.settimeout(5)
    print(s.recv(1024).strip('b'))


def main():
    ip = input("Enter IP address: ")
    port = int(input("Enter port number: "))
    banner(ip, port)


main()

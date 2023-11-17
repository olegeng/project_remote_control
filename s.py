import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.0.108', 1234))
while True:
    client.send(input('Enter command: ').encode('utf-8'))
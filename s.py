import socket, requests
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket
client.connect(('46.118.186.247', 1234)) #connect to testik.py
received_message = client.recv(1024).decode('utf-8')
print(received_message)
while True:
    client.send(input('Enter command: ').encode('utf-8')) #send command
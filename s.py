import socket, requests
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket

client.connect(('176.8.62.61', 1234)) #connect to testik.py
while True:
    client.send(input('Enter command: ').encode('utf-8')) #send command
import socket, webbrowser
from tkinter import *
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234))
server.listen()
print(socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234)
root = Tk()  # create a root widget
root.title("Your IP to enter in bot")
root.configure(background="yellow")
root.minsize(200, 200)  # width, height
root.maxsize(500, 500)
root.geometry("300x300+50+50")  # width x height + x + y
text = Label(root, text=(socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234)[0])
text.pack()
text1 = Label(root, text=('In order to continue - close this window'))
text1.pack()
print('+++')
root.mainloop()
while True:
    user, adres = server.accept()
    print('+!+')
    while True:
        data = user.recv(1024).decode('utf-8').lower()
        print('!!!')
        if data=='youtube':
            print('CONTACT')
            webbrowser.open('https://www.youtube.com/')









# import uuid
# print(uuid.getnode())
# print(hex(uuid.getnode()))
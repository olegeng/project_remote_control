import socket, webbrowser, requests
from tkinter import *
response = requests.get('https://httpbin.org/ip') #Взяти зовнішній IP
ip = response.json().get('origin', '')            # також
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234)) #внутрішній IP, port
server.listen() #Заставити сервер слухати команди
print(socket.gethostbyname_ex(socket.gethostname())[-1][-1]) #Внутрішній IP в консоль
#тут вставка з ткінтера
#root.mainloop()
while True:
    user, adres = server.accept()
    print('+!+')
    while True:
        data = user.recv(1024).decode('utf-8').lower()
        print('!!!')
        if data=='youtube':
            print('CONTACT')
            webbrowser.open('https://www.youtube.com/')




# root = Tk()  # create a root widget
                                        # root.title("Your IP to enter in bot")
                                        # root.configure(background="yellow")
                                        # root.minsize(200, 200)  # width, height
                                        # root.maxsize(500, 500)
                                        # root.geometry("300x300+50+50")  # width x height + x + y
                                        # text = Label(root, text=(socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234)[0])
                                        # text.pack()
                                        # text1 = Label(root, text=('In order to continue - close this window'))
                                        # text1.pack()
                                        # text2 = Label(root, text=(f'{ip}'))
                                        # text2.pack()




# import uuid
# print(uuid.getnode())
# print(hex(uuid.getnode()))
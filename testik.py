import socket, webbrowser, requests, uuid, subprocess
# from tkinter import *
response = requests.get('https://httpbin.org/ip') #Взяти зовнішній IP
ip = response.json().get('origin', '')  # також
print(ip)
def s():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234)) #внутрішній IP, port
    server.listen(3) #Заставити сервер слухати команди
    print(socket.gethostbyname_ex(socket.gethostname())[-1][-1]) #Внутрішній IP в консоль
    print(hex(uuid.getnode())[2:])
    #тут вставка з ткінтера
    #root.mainloop()
    while True:
        user, adres = server.accept()
        user.sendall(f'{ip}!{socket.gethostbyname_ex(socket.gethostname())[-1][-1]}!{hex(uuid.getnode())[2:]}'.encode('utf-8'))
        print('+!+')
        while True:
            data = user.recv(1024).decode('utf-8').lower()
            print(data)
            if '_$_' in data:                               #for files
                                                            #to be continued
                pass
            elif '$_$' in data:                             #for webbrowser
                print('CONTACT')
                data=data.split('$_$')
                webbrowser.open(data[1])
            elif data=='/disconect':
                return '200'
            else:
                print('###')
                print(run_command(data))

def run_command(command):
    try:
        # Викликайте команду за допомогою Popen
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Очікуйте завершення процесу та отримайте вивід
        output, error = process.communicate()
        output = ' '.join(output.split())
        output=output[output.index('<DIR>')::]
        #output = ' '.join(output.split('<DIR>'))
        # Перевірте код виходу
        if process.returncode == 0:
            return {"output": output, "error": error, "success": True}
        else:
            return {"output": output, "error": error, "success": False, "exit_code": process.returncode}

    except Exception as e:
        return {"output": None, "error": str(e), "success": False}

while True:
    try:
        if s()=='200':
            break
    except ConnectionAbortedError:
        continue



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
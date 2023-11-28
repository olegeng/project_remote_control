# started 14.11.2023
import os, shutil, qrcode, telebot, socket, requests
# from PIL import Image
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


token = "6899953920:AAHhYeCEMHb3twGmCDcVuVmZym1AqvJeysE"
bot=telebot.TeleBot(token)


class Managing:
    def __init__(self):
        pass

    def __str__(self):
        return f'This class was created in order to make contact with server'

    def client_con(self, message):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket
        client.connect(('46.118.186.247', 1234))#connect to testik.py
        #self.received_message = client.recv(1024).decode('utf-8')
        #self.command_to_send = input('Enter command: ')
        self.command_to_send = message.text
        client.send(self.command_to_send.encode('utf-8'))#send command
        client.close()
        return None


def make_zip(directory_to_zip=f'{os.path.dirname(__file__)}/send_to_user', zip_file_path = f'{os.path.dirname(__file__)}/zipka.zip'):
    shutil.make_archive(zip_file_path.split('.zip')[0], 'zip', directory_to_zip)
    print('ZIP was made!')



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Let\'s do it!\n In order to connect you need to download and execute this one beneath')
    bot.send_message(message.chat.id, 'After that you need to read instruction from /help command')
    make_zip()
    with open("zipka.zip", "rb") as misc:
        bot.send_document(message.chat.id,misc)

@bot.message_handler(commands=['help'])
def explanation(message):
    bot.send_message(message.chat.id, 'Tap on one of this links (which one will work): http://192.168.0.1/ \\nhttp://192.168.1.1')
    bot.send_message(message.chat.id, 'Authorize > Settings > Port Forwarding > Add')
    bot.send_message(message.chat.id, 'Set a name, pick your device, Internal port: 1234, External port: 1234, Protocols: Everything')

@bot.message_handler(commands=['menu'])
def menu_of_bot(message):
    bot.send_message(message.chat.id, 'Let\'s decide what would you like to do', reply_markup=markup_inline())

@bot.message_handler(content_types='text')
def menu_of_connection(message):
    connection.client_con(message)

def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.row_width = 4
    spis_1 = ['Connect!', 'Disconnect', 'Bye']
    for z in spis_1:
        markup.add(
            InlineKeyboardButton(z, callback_data=z),
        )
    return markup

@bot.callback_query_handler(func=lambda message: True)
def callback_query(call):
    if call.data == 'Connect!':
        print('+')
        connection.client()
# qr = qrcode.QRCode(version=2, box_size=10, border=9, error_correction=qrcode.constants.ERROR_CORRECT_H)
# data = "https://web.telegram.org/k/#@hrytsko_managebot"
# qr.add_data(data)
# qr.make(fit=True)
# img = qr.make_image(fill_color="black", back_color="grey")
# img.save("code7.png")
# qr_to_send = open('code7.jpg', 'rb')
# bot.send_photo(cid, qr_to_send)
#
# with Image.open('code7.png') as imga:
#     imga.show()


# class Finder:
#     def __init__(self, name):
#         self.namek = name
#
#     def file(self):
#         for root, dirs, files in os.walk('D:/'):
#             print(files)
#             if self.name in files:
#                 return f'{root}/{self.name}'
#         for root, dirs, files in os.walk('C:/'):
#             if self.name in files:
#                 return f'{root}/{self.name}'
#
#     def dirs(self):
#         for root, dirs, files in os.walk('D:/'):
#             if self.name in dirs:
#                 return f'{root}/{self.name}'
#         for root, dirs, files in os.walk('C:/'):
#             if self.name in dirs:
#                 return f'{root}/{self.name}'
connection = Managing()
bot.infinity_polling()
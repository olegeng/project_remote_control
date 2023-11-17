#started 14.11.2023
import os, shutil, qrcode, telebot
from PIL import Image
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = "6899953920:AAHhYeCEMHb3twGmCDcVuVmZym1AqvJeysE"
bot=telebot.TeleBot(token)

def make_zip(directory_to_zip = f'{os.path.dirname(__file__)}/send_to_user', zip_file_path = f'{os.path.dirname(__file__)}/zipka.zip'):
    shutil.make_archive(zip_file_path.split('.zip')[0], 'zip', directory_to_zip)
    print('ZIP was made!')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Let\'s do it!\n In order to connect you need to download and execute this one beneath')
    bot.send_message(message.chat.id, 'After that you need to inform me about your IP address which script show you')
    make_zip()
    with open("zipka.zip", "rb") as misc:
        bot.send_document(message.chat.id,misc)


@bot.callback_query_handler(func=lambda message: True)
def callback_query(call):
    pass
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


class Finder:
    def __init__(self, name):
        self.name = name

    def file(self):
        for root, dirs, files in os.walk('D:/'):
            print(files)
            if self.name in files:
                return f'{root}/{self.name}'
        for root, dirs, files in os.walk('C:/'):
            if self.name in files:
                return f'{root}/{self.name}'

    def dirs(self):
        for root, dirs, files in os.walk('D:/'):
            if self.name in dirs:
                return f'{root}/{self.name}'
        for root, dirs, files in os.walk('C:/'):
            if self.name in dirs:
                return f'{root}/{self.name}'
bot.infinity_polling()
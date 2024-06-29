import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()

#Conexión con nuestro bot
TOKEN = os.getenv('TELEGRAM_BOT_KEY')
bot = telebot.TeleBot(TOKEN)

#Creación de comandos /start y /help

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Hola! Soy tu bot.')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,'Puedes escribir cosas y yo las repetire.')

# @bot.message_handler(func=lambda m:True)
# def echo_all(message):
#     bot.reply_to(message,message.text)

@bot.message_handler(commands=['opcion'])
def send_options(message):
    #Creación de grid para los botones.
    markup = types.InlineKeyboardMarkup(row_width=2)
    #Creación de los botones.
    btn_si = types.InlineKeyboardButton('Si', callback_data='opcion_si')
    btn_no = types.InlineKeyboardButton('No', callback_data='opcion_no')
    #Anadir botones a grid.
    markup.add(btn_si,btn_no)
    #bot.reply_to(message,'¿Te apetece?', reply_markup=markup)
    bot.send_message(message.chat.id, "¿Te gusta la opción?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'opcion_si':
        #bot.send_message(call.message.chat.id, "Perfecto!")
        bot.answer_callback_query(call.id, text="Perfecto!")
    elif call.data == 'opcion_no':
        bot.answer_callback_query(call.id, text="No pasa nada!")
        #bot.send_message(call.message.chat.id, "No pasa nada.")

@bot.message_handler(commands=['foto'])
def send_fotos(message):
    img_url = 'https://pbs.twimg.com/profile_images/1806568875875561473/PF0vueCt_400x400.jpg'
    bot.send_photo(chat_id=message.chat.id, photo=img_url, caption="Dame tu dinero facha")
if __name__ == "__main__":
    bot.polling(none_stop=True)
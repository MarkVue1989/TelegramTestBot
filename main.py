import telebot

#Conexión con nuestro bot
TOKEN = '7191696119:AAF9BuOhdTyPJhNbwLjDeSWjrNsZivpZUPQ'
bot = telebot.TeleBot(TOKEN)

#Creación de comandos /start y /help

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Hola! Soy tu bot.')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,'Puedes escribir cosas y yo las repetire.')

@bot.message_handler(func=lambda m:True)
def echo_all(message):
    bot.reply_to(message,message.text)

if __name__ == "__main__":
    bot.polling(none_stop=True)
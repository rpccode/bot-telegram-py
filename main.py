import telebot

bot = telebot.TeleBot("5926816130:AAF0YddnlJ64rj4OxpX3VtT-0BNIA_TtN5A")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()

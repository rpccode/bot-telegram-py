from config import * # importamos el token
import telebot
import time
import random
import threading
# Botones inline
from telebot.types import InlineKeyboardMarkup # Crea botones inline
from telebot.types import InlineKeyboardButton # Define los botones inline

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])

# Funciones de los comandos
def cmd_start(message):
    # Dar la bienvenida al usuario del bot
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, "Hola "+message.chat.first_name+", aqui estan todos los comandos que puedes usar, para controlar el bot.\n\n/start - Mostrar todos los comandos\n\n/buttons - Te muestra los botones para realizar las consultas\n\n/info - Ofrece informacion sobre el bot\n\n/help - Te dara una pequeña descripcion de como puedes interactuar con el bot")
    #print(message.chat.id)

# Responden al comando buttons
@bot.message_handler(commands=["buttons"])

# Responde al comando button
def cmd_button(message):
    bot.send_chat_action(message.chat.id, "typing")
    # Mostrar un mensaje con botones inline, debajo del mensaje
    markup = InlineKeyboardMarkup(row_width=1) # Numero de botones por fila (3 por defecto)
    # Botones
    b1 = InlineKeyboardButton("NUESTROS PRODUCTOS", callback_data="b1")
    b2 = InlineKeyboardButton("RESERVA DE PRODUCTOS", callback_data="b2")
    b3 = InlineKeyboardButton("STATUS DE SU RESERVA", callback_data="b3")
    b4 = InlineKeyboardButton("CANCELACION SU RESERVA", callback_data="b4")
    b_cerrar = InlineKeyboardButton("CERRAR", callback_data="cerrar")
    markup.add(b1, b2, b3, b4, b_cerrar)
    bot.send_message(message.chat.id, "SUPERMERCADO LA ESPERANZA", reply_markup=markup)

# Responde al comando info
@bot.message_handler(commands=["info"])

def cmd_info(message):
    # Ofrece informacion sobre el bot y su autor
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, "Hola "+message.chat.first_name+", aqui esta la informacion sobre Supermercado La Esperanza.\n\n")
    # Mostrar un mensaje con botones inline, debajo del mensaje
    markup2 = InlineKeyboardMarkup(row_width=2) # Numero de botones por fila (3 por defecto)
    # Botones
    bs1 = InlineKeyboardButton("HORARIOS", bot.send_message(message.chat.id, "Domingo\t08:00:00AM - 02:00:00PM\nLunes\t\t\t08:00:00AM - 10:00:00PM\nMartes\t\t\t08:00:00AM - 10:00:00PM\nMiercoles\t\t\t08:00:00AM - 10:00:00PM\nJueves\t\t\t08:00:00AM - 10:00:00PM\nViernes\t\t\t08:00:00AM - 10:00:00PM\nSabado\t\t\t08:00:00AM - 02:00:00PM\n"))
    bs2 = InlineKeyboardButton("TELEFONOS", bot.send_message(message.chat.id, "Telefonos disponibles:\n\nTelefono #1: (809) 233-1010\nTelefono #2: (809) 575-6000\nTelefono #3: (809) 241-6262\n"))
    bs3 = InlineKeyboardButton("PAGINA WEB", url="https://laesperanzaca.com/supermarket/")
    bs4 = InlineKeyboardButton("FACEBOOK", url="https://web.facebook.com/pages/category/Specialty-Grocery-Store/La-Esperanza-Food-Center-770731589767698/?_rdc=1&_rdr")
    bs5 = InlineKeyboardButton("GMAIL", url="https://mail.google.com/mail/u/0/?tab=rm&ogbl")
    markup2.add(bs1, bs2, bs3, bs4, bs5)
    bot.send_message(message.chat.id, "Informacion del Supermercado La Esperanza", reply_markup=markup2)

# enviar correo
def send_email():
    pass

def recibir_mensajes():
    bot.infinity_polling()

if __name__ == '__main__':
    print("Bot iniciando...")
    # Configurar los comandos de nuestro bot
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Te muestra todos los comandos disponibles"),
        telebot.types.BotCommand("/buttons", "Te muestra los botones para realizar las consultas"),
        telebot.types.BotCommand("/info", "Ofrece informacion sobre el bot"),
        telebot.types.BotCommand("/help", "Ofrece ayuda sobre el bot")
    ])
    print("Bot en funcionamiento...")
    # Usando threading
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    bot.send_message(MI_CHAT_ID, "Bienvenido a Supermercado La Esperanza Bot, es un gusto tenerte por aqui!!.\n\nQue puede hacer este bot por ti?\n\nSupermercado La Esperanza es un bot creado para facilitar consultas, compras y reservas de nuestros productos disponibles.\n\nContacto directo via nuestros servicios de comunicacion:\n\nTelefono: 809-123-4567\nCorreo Electronico: supermercadolaesperanza@gmail.com\nDireccion: Ave. Estrella Sadhala, 51000, Santiago de los Caballeros")

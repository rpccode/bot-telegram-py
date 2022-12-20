from config import *  # importamos el token
import telebot
import time
import random
import threading
# Botones inline
from telebot.types import InlineKeyboardMarkup  # Crea botones inline
from telebot.types import InlineKeyboardButton  # Define los botones inline

bot = telebot.TeleBot(TOKEN)

# Responden al comando buttons


@bot.message_handler(commands=["buttons"])
# Responde al comando button
def cmd_button(message):
    bot.send_chat_action(message.chat.id, "typing")
    # Mostrar un mensaje con botones inline, debajo del mensaje
    # Numero de botones por fila (3 por defecto)
    markup = InlineKeyboardMarkup(row_width=1)
    # Botones
    b1 = InlineKeyboardButton("NUESTROS PRODUCTOS", callback_data="b1")
    b2 = InlineKeyboardButton("RESERVA DE PRODUCTOS", callback_data="b2")
    b3 = InlineKeyboardButton("STATUS DE SU RESERVA", callback_data="b3")
    b4 = InlineKeyboardButton("CANCELACION SU RESERVA", callback_data="b4")
    markup.add(b1, b2, b3, b4)
    bot.send_message(
        message.chat.id, "SUPERMERCADO LA ESPERANZA", reply_markup=markup)


@bot.message_handler(commands=['start'])
# Funciones de los comandos
def cmd_start(message):
    # Dar la bienvenida al usuario del bot
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, "Hola "+message.chat.first_name+", aqui estan todos los comandos que puedes usar, para controlar el bot.\n\n/start - Mostrar todos los comandos\n\n/buttons - Te muestra los botones para realizar las consultas\n\n/info - Ofrece informacion sobre el bot\n\n/help - Te dara una pequeña descripcion de como puedes interactuar con el bot")
    # Mostrar un mensaje con botones inline, debajo del mensaje
    cmd_button(message)

# Responde al comando info


@bot.message_handler(commands=["info"])
def cmd_info(message):
    # Ofrece informacion sobre el bot y su autor
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, "Hola "+message.chat.first_name +
                 ", aqui esta la informacion sobre Supermercado La Esperanza.\n\n")
    # Messages
    bot.send_message(
        message.chat.id, "DIRECCION.\n Ave. Estrella Sadhala, 51000, Santiago de los Caballeros")
    bot.send_message(
        message.chat.id, "CORREO ELECTRONICO.\n: supermercadolaesperanza@gmail.com")
    bot.send_message(message.chat.id, "HORARIOS\n\nDomingo\t08:00:00AM - 02:00:00PM\nLunes\t\t\t08:00:00AM - 10:00:00PM\nMartes\t\t\t08:00:00AM - 10:00:00PM\nMiercoles\t\t\t08:00:00AM - 10:00:00PM\nJueves\t\t\t08:00:00AM - 10:00:00PM\nViernes\t\t\t08:00:00AM - 10:00:00PM\nSabado\t\t\t08:00:00AM - 02:00:00PM\n")
    bot.send_message(
        message.chat.id, "TELEFONOS\n\nTelefonos disponibles:\n\nTelefono #1: (809) 233-1010\nTelefono #2: (809) 575-6000\nTelefono #3: (809) 241-6262\n")
    bot.send_message(message.chat.id, "[PAGINA WEB](https://laesperanzaca.com/supermarket/)",
                     parse_mode="MarkDownV2", disable_web_page_preview=True)
    bot.send_message(message.chat.id, "[FACEBOOK](https://web.facebook.com/pages/category/Specialty-Grocery-Store/La-Esperanza-Food-Center-770731589767698/?_rdc=1&_rdr)",
                     parse_mode="MarkDownV2", disable_web_page_preview=True)
    bot.send_message(message.chat.id, "[GMAIL](https://mail.google.com/mail/u/0/?tab=rm&ogbl)",
                     parse_mode="MarkDownV2", disable_web_page_preview=True)

# Responden al comando help


@bot.message_handler(commands=["help"])
def cmd_help(message):
    # Ofrece ayuda sobre como utilizar el bot
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, "Hola este es el apartado de ayuda:Digitar los siguientes comandos en el chat\n\n/start : Para poder contactar con el bot puedes utilizar el comando .\n /buttons : Para ver los botones disponibles.\n /info : Para ver informacion detallada sobre El Supermercado La Esperanza.\n  /help : Verificar comandos.")


# Introduccion al escribir
greetings = ['Hola!! 🤠👋🏼', 'Buenos noches!! 🤓🌚', 'Hola!, que tal? 🧑🏻', 'Klk!! 🤣', 'Buenas tardes!! 😄🌞', 'Saludos mi estimad@!! 😏👌🏼',
             'Encantado de hablar contigo!! 😜', 'Saludos!! 😌', 'Guao tengo visita!! 😆', 'Es agradable hablar con alguien!, tengo mucho tiempo solo 😔']
# Responder a los mensajes sin poner comandos


@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    num = random.randint(0, 9)
    # Gestiona los mensajes que recibe
    # Esta funcion recibe dos parametros el chat id, tiene un identificador unico y el mensaje
    if message.text and message.text.startswith("/"):
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "ERROR: Este comando no existe!!")
    else:
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, greetings[num]+"\n"+message.chat.first_name +
                         "!! Aqui te muestro las consultas que puedes realizar.")
        # Mostrar un mensaje con botones inline, debajo del mensaje
        cmd_button(message)

# Funcion para cerrar


@bot.callback_query_handler(func=lambda call: True)
def respuesta_botones_inline(call):
    # Gestionara las acciones de los botones callback_data
    cid = call.from_user.id
    mid = call.message.id
    if call.data == "b1":
        example()
    if call.data == "b2":
        example()
    if call.data == "b3":
        example()
    if call.data == "b3":
        example()

# Example


def example():
    print("Se uso...")

# enviar correo


def send_email():
    pass


def recibir_mensajes():
    bot.infinity_polling()


if __name__ == '__main__':
    print("Bot iniciando...")
    # Configurar los comandos de nuestro bot
    bot.set_my_commands([
        telebot.types.BotCommand(
            "/start", "Te muestra todos los comandos disponibles"),
        telebot.types.BotCommand(
            "/buttons", "Te muestra los botones para realizar las consultas"),
        telebot.types.BotCommand("/info", "Ofrece informacion sobre el bot"),
        telebot.types.BotCommand("/help", "Ofrece ayuda sobre el bot")
    ])
    print("Bot en funcionamiento...")
    # Usando threading
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    bot.send_message(MI_CHAT_ID, "Bienvenido a Supermercado La Esperanza Bot, Soy su asistente virtual es un gusto tenerte por aqui!!.\nQue puede hacer por ti?\n\nSupermercado La Esperanza es un bot creado para facilitar consultas, compras y reservas de nuestros productos disponibles. Si buscas mas informacion digite /start")

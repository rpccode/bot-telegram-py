from data import *
from db import *
from config import *  # importamos el token
import telebot
import asyncio
import time
import random
import threading
import asyncio
# Botones inline
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton  # Crea botones inline
from telebot.types import ReplyKeyboardMarkup, ForceReply  # Define los botones inline

bot = telebot.TeleBot(TOKEN)
bot.set_webhook()


# Responden al comando buttons
@bot.message_handler(commands=["buttons"])
# Responde al comando button
def cmd_button(message):
    bot.send_chat_action(message.chat.id, "typing")
    # Mostrar un mensaje con botones inline, debajo del mensaje
    markup = InlineKeyboardMarkup(row_width=1)  # Numero de botones por fila (3 por defecto)
    # Botones
    b1 = InlineKeyboardButton("NUESTROS PRODUCTOS", callback_data="b1")
    b2 = InlineKeyboardButton("RESERVA DE PRODUCTOS", callback_data="b2")
    b3 = InlineKeyboardButton("STATUS DE SU RESERVA", callback_data="b3")
    b4 = InlineKeyboardButton("CANCELACION SU RESERVA", callback_data="b4")
    markup.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, "SUPERMERCADO LA ESPERANZA", reply_markup=markup)


@bot.message_handler(commands=['start'])
# Funciones de los comandos
def cmd_start(message):
    # Dar la bienvenida al usuario del bot
    bot.send_chat_action(message.chat.id, "typing")
    print(message.chat)
    bot.reply_to(message,
                 "Hola " + message.chat.first_name + ", aqui estan todos los comandos que puedes usar, para controlar "
                                                     "el bot.\n\n/start - Mostrar todos los comandos\n\n/buttons - Te "
                                                     "muestra los botones para realizar las consultas\n\n/info - "
                                                     "Ofrece informacion sobre el bot\n\n/help - Te dara una pequeña "
                                                     "descripcion de como puedes interactuar con el bot")
    # Mostrar un mensaje con botones inline, debajo del mensaje
    cmd_button(message)


# Responde al comando info
@bot.message_handler(commands=["info"])
def cmd_info(message):
    # Ofrece información sobre el bot y su autor
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message,
                 "Hola " + message.chat.first_name + ", aqui esta la informacion sobre Supermercado La Esperanza.\n\n")
    # Messages
    bot.send_message(message.chat.id, "DIRECCION.\n Ave. Estrella Sadhala, 51000, Santiago de los Caballeros")
    bot.send_message(message.chat.id, "CORREO ELECTRONICO.\n: supermercadolaesperanza@gmail.com")
    bot.send_message(message.chat.id,
                     "HORARIOS\n\nDomingo\t08:00:00AM - 02:00:00PM\nLunes\t\t\t08:00:00AM - "
                     "10:00:00PM\nMartes\t\t\t08:00:00AM - 10:00:00PM\nMiercoles\t\t\t08:00:00AM - "
                     "10:00:00PM\nJueves\t\t\t08:00:00AM - 10:00:00PM\nViernes\t\t\t08:00:00AM - "
                     "10:00:00PM\nSabado\t\t\t08:00:00AM - 02:00:00PM\n")
    bot.send_message(message.chat.id,
                     "TELEFONOS\n\nTelefonos disponibles:\n\nTelefono #1: (809) 233-1010\nTelefono #2: (809) "
                     "575-6000\nTelefono #3: (809) 241-6262\n")
    bot.send_message(message.chat.id, "[PAGINA WEB](https://laesperanzaca.com/supermarket/)", parse_mode="MarkDownV2",
                     disable_web_page_preview=True)
    bot.send_message(message.chat.id,
                     "[FACEBOOK](https://web.facebook.com/pages/category/Specialty-Grocery-Store/La-Esperanza-Food"
                     "-Center-770731589767698/?_rdc=1&_rdr)",
                     parse_mode="MarkDownV2", disable_web_page_preview=True)
    bot.send_message(message.chat.id, "[GMAIL](https://mail.google.com/mail/u/0/?tab=rm&ogbl)", parse_mode="MarkDownV2",
                     disable_web_page_preview=True)


# Responden al comando help
@bot.message_handler(commands=["help"])
def cmd_help(message):
    # Ofrece ayuda sobre como utilizar el bot
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message,
                 "Hola este es el apartado de ayuda:Digitar los siguientes comandos en el chat\n\nPara poder "
                 "contactar con el bot puedes utilizar el comando /start.\nPara ver los botones disponibles "
                 "/buttons.\nPara ver informacion detallada sobre El Supermercado La Esperanza /info.\n Verificar "
                 "comandos /help.")


# Introduction al escribir
greetings = ['Hola!! 🤠👋🏼', 'Buenos noches!! 🤓🌚', 'Hola!, que tal? 🧑🏻', 'Klk!! 🤣', 'Buenas tardes!! 😄🌞',
             'Saludos mi estimad@!! 😏👌🏼', 'Encantado de hablar contigo!! 😜', 'Saludos!! 😌', 'Guao tengo visita!! 😆',
             'Es agradable hablar con alguien!, tengo mucho tiempo solo 😔']


# Responder a los mensajes sin poner comandos
# @bot.message_handler(content_types=["text"])
# def bot_mensajes_texto(message):
#     num = random.randint(0, 9)
#     # Gestiona los mensajes que recibe
#     # Esta funcion recibe dos parameters el chat id, tiene un identificador unico y el mensaje
#     if message.text and message.text.startswith("/"):
#         bot.send_chat_action(message.chat.id, "typing")
#         bot.send_message(message.chat.id, "ERROR: Este comando no existe!!")
#     if message.text != 'Black' or message.text != 'Blue' or message.text != 'Grey' or message.text != 'Multi' or message.text != 'Red' or message.text != 'Silver' or message.text != 'Silver/Black' or message.text != 'White,Yellow':
#         bot.send_chat_action(message.chat.id, "typing")
#         bot.send_message(message.chat.id, greetings[
#             num] + "\n" + message.chat.first_name + "!! Aqui te muestro las consultas que puedes realizar.")
#         # Mostrar un mensaje con botones inline, debajo del mensaje
#         cmd_button(message)


# Funcion para cerrar
@bot.callback_query_handler(func=lambda call: True)
def respuesta_botones_inline(call):
    # Gestionará las acciones de los botones callback_data
    cid = call.from_user.id
    mid = call.message.id
    chat = call.message.chat.id
    print(call.data)
    if call.data == "b1":
        botones_producto(cid, mid, chat)
    elif call.data == 'esp':
        boton_esp(chat)
    elif call.data == 'col':
        respuesta_botones_de_producto_buscar_color(call)
        bot.send_message(call.message.chat.id, 'Elija una Opcion?')
    elif call.data == 'tam':
        print('ENTRO')
        respuesta_botones_de_producto_buscar_size(chat)
    elif call.data == 'pe':
        print('ENTRO')
        respuesta_botones_de_producto_buscar_weigth(chat)



@bot.callback_query_handler(func=lambda call: True)
def respuesta_botones_de_producto_buscar(call):
    # Gestionará las acciones de los botones callback_data
    cid = call.from_user.id
    mid = call.message.id
    chat = call.message.chat.id
    print(min)
    if call.data == "esp":
        print('entro')


def respuesta_botones_de_producto_buscar_color(call):
    # Gestionara las acciones de los botones callback_data
    cid = call.from_user.id
    mid = call.message.id
    chat = call.message.chat.id
    print(min)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)  # Numero de botones por fila (3 por defecto)
    markup.add('Black', 'Blue', 'Grey', 'Multi', 'Red', 'Silver', 'Silver/Black', 'White', 'Yellow')
    msg = bot.send_message(chat, "Por el Momento Solo Contamos con los Siguientes Colores:\n\n "
                                 "Black,Blue,Grey,Multi,Red,Silver,Silver/Black,White,Yellow"
                                 "", reply_markup=markup)
    bot.register_next_step_handler(msg, producto_buscar_color)


def producto_buscar_color(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)
    markup.add('Buscar', 'volver al menu')
    color = message.text
    productos = traer_productos_por_color(color)
    for producto in productos:
        texto = 'Detalles de Productos:\n\n '
        texto += f'<code>Numero del producto: </code>{producto[2]}\n'
        texto += f'<code>Nombre del producto: </code>{producto[1]}\n'
        texto += f'<code>Color del producto: </code>{producto[3]}\n'
        texto += f'<code>Precio del producto: </code>{producto[5]}$\n'
        texto += f'<code>Tamaño del producto: </code>{producto[6]}\n'
        texto += f'<code>Ancho del producto: </code>{producto[7]} cm\n'
        bot.send_message(message.chat.id, texto, parse_mode='html')
    msg = bot.send_message(message.chat.id, 'Desea seguir Buscando?', reply_markup=markup)
    bot.register_next_step_handler(msg, volver_a_preguntar_color)


def volver_a_preguntar_color(message):
    cid = message.from_user.id
    mid = message.id
    if message.text == 'Buscar':
        bot.delete_message(message.chat.id, message.message_id)
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                     row_width=3)  # Numero de botones por fila (3 por defecto)
        markup.add('Black', 'Blue', 'Grey', 'Multi', 'Red', 'Silver', 'Silver/Black', 'White', 'Yellow')
        msg = bot.send_message(message.chat.id, "Por el Momento Solo Contamos con los Siguientes Colores:\n\n "
                                                "Black,Blue,Grey,Multi,Red,Silver,Silver/Black,White,Yellow"
                                                "", reply_markup=markup)
        bot.register_next_step_handler(msg, producto_buscar_color)


    else:
        cid = message.from_user.id
        mid = message.id
        chat = message.chat.id
        botones_producto(cid, mid, chat)


def respuesta_botones_de_producto_buscar_size(chat):
    # Gestionara las acciones de los botones callback_data

    print(min)
    markup = ForceReply()  # Numero de botones por fila (3 por defecto)
    msg = bot.send_message(chat, "Por el Momento Solo Contamos con los Siguientes Size:\n\n "
                                 "S\t""M\t""xl\t" ' o puede seleccionar un Size de forma Numerica ej: 33 '
                                 "", reply_markup=markup)
    bot.register_next_step_handler(msg, producto_buscar_size)


def producto_buscar_size(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)
    markup.add('Buscar', 'volver al menu')
    size = message.text
    productos = traer_productos_por_size(size)
    for producto in productos:
        texto = 'Detalles de Productos:\n\n '
        texto += f'<code>Numero del producto: </code>{producto[2]}\n'
        texto += f'<code>Nombre del producto: </code>{producto[1]}\n'
        texto += f'<code>Color del producto: </code>{producto[3]}\n'
        texto += f'<code>Precio del producto: </code>{producto[5]}$\n'
        texto += f'<code>Tamaño del producto: </code>{producto[6]}\n'
        texto += f'<code>Ancho del producto: </code>{producto[7]} cm\n'
        bot.send_message(message.chat.id, texto, parse_mode='html')
    msg = bot.send_message(message.chat.id, 'Desea seguir Buscando?', reply_markup=markup)
    bot.register_next_step_handler(msg, volver_a_preguntar_size)


def volver_a_preguntar_size(message):
    cid = message.from_user.id
    mid = message.id
    chat = message.chat.id
    if message.text == 'Buscar':
        respuesta_botones_de_producto_buscar_size(chat)

    else:
        cid = message.from_user.id
        mid = message.id
        chat = message.chat.id
        botones_producto(cid, mid, chat)


def respuesta_botones_de_producto_buscar_weigth(chat):
    # Gestionará las acciones de los botones callback_data

    print(min)
    markup = ForceReply()  # Número de botones por fila (3 por defecto)
    msg = bot.send_message(chat, 'Que tamaño desea? '
                                 "", reply_markup=markup)
    bot.register_next_step_handler(msg, producto_buscar_size)


def producto_buscar_weigth(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)
    markup.add('Buscar', 'volver al menu')
    size = message.text
    productos = traer_productos_por_size(size)
    for producto in productos:
        texto = 'Detalles de Productos:\n\n '
        texto += f'<code>Numero del producto: </code>{producto[2]}\n'
        texto += f'<code>Nombre del producto: </code>{producto[1]}\n'
        texto += f'<code>Color del producto: </code>{producto[3]}\n'
        texto += f'<code>Precio del producto: </code>{producto[5]}$\n'
        texto += f'<code>Tamaño del producto: </code>{producto[6]}\n'
        texto += f'<code>Ancho del producto: </code>{producto[7]} cm\n'
        bot.send_message(message.chat.id, texto, parse_mode='html')
    msg = bot.send_message(message.chat.id, 'Desea seguir Buscando?', reply_markup=markup)
    bot.register_next_step_handler(msg, volver_a_preguntar_weigth)


def volver_a_preguntar_weigth(message):
    cid = message.from_user.id
    mid = message.id
    chat = message.chat.id
    if message.text == 'Buscar':
        respuesta_botones_de_producto_buscar_weigth(chat)

    else:
        cid = message.from_user.id
        mid = message.id
        chat = message.chat.id
        botones_producto(cid, mid, chat)


# Example
def example(call):
    productos = traer_productos_formateados()
    for producto in productos:
        texto = 'Detalles de Productos:\n\n '
        texto += f'<code>Numero del producto: </code>{producto[2]}\n'
        texto += f'<code>Nombre del producto: </code>{producto[1]}\n'
        texto += f'<code>Color del producto: </code>{producto[3]}\n'
        texto += f'<code>Precio del producto: </code>{producto[5]}$\n'
        texto += f'<code>Tamaño del producto: </code>{producto[6]}\n'
        texto += f'<code>Ancho del producto: </code>{producto[7]} cm\n'
        bot.send_message(call.message.chat.id, texto, parse_mode='html')


def botones_producto(cid, mid, chat):
    markup = InlineKeyboardMarkup(row_width=1)  # Numero de botones por fila (3 por defecto)
    # Botones
    b1 = InlineKeyboardButton("Especificacciones del Producto", callback_data="esp")
    b2 = InlineKeyboardButton("Categoria de  PRODUCTOS", callback_data="cat")
    b3 = InlineKeyboardButton("Precio de Producto", callback_data="pre")
    b4 = InlineKeyboardButton("Nombre del Producto", callback_data="nom")
    b5 = InlineKeyboardButton("Numero del Producto", callback_data="num")
    markup.add(b1, b2, b3, b4, b5)
    bot.send_message(chat, "Puede Consultar sus productos por la siguiente Opciones",
                     reply_markup=markup)
    bot.delete_message(cid, mid)


def boton_esp(chat):
    markup = InlineKeyboardMarkup(row_width=1)  # Número de botones por fila (3 por defecto)
    # Botones
    b1 = InlineKeyboardButton("color del Producto", callback_data="col")
    b2 = InlineKeyboardButton("Tamaño del  PRODUCTOS", callback_data="tam")
    b3 = InlineKeyboardButton("Peso del Producto", callback_data="pe")
    markup.add(b1, b2, b3)
    bot.send_message(chat, "Puede Consultar sus productos por la siguiente Opciones", reply_markup=markup)


# enviar correo
def send_email():
    print("Se uso...")
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
    bot.send_message(MI_CHAT_ID,
                     "Bienvenido a Supermercado La Esperanza Bot, Soy su asistente virtual es un gusto tenerte por "
                     "aqui!!.\nQue puede hacer por ti?\n\nSupermercado La Esperanza es un bot creado para facilitar "
                     "consultas, compras y reservas de nuestros productos disponibles. Si buscas mas informacion "
                     "digite /start")

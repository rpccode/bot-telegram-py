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
usuarios = {}
usuario = {}



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
    bot.send_message(message.chat.id, "Tienda de Bike  LA ESPERANZA", reply_markup=markup)


def cmd_button_orden_estado(chat):
    bot.send_chat_action(chat, "typing")
    # Mostrar un mensaje con botones inline, debajo del mensaje
    markup = InlineKeyboardMarkup(row_width=1)  # Numero de botones por fila (3 por defecto)
    # Botones
    b1 = InlineKeyboardButton("En Progreso", callback_data="1")
    b2 = InlineKeyboardButton("Aprovado", callback_data="2")
    b3 = InlineKeyboardButton("Pedido pendiente", callback_data="3")
    b4 = InlineKeyboardButton("Rechazada", callback_data="4")
    b5 = InlineKeyboardButton("Enviada", callback_data="5")
    b6 = InlineKeyboardButton("Canceladas", callback_data="6")
    markup.add(b1, b2, b3, b4, b5, b6)
    bot.send_message(chat, "Verifica el Estado de tu reserva:", reply_markup=markup)


@bot.message_handler(commands=['start'])
# Funciones de los comandos
def cmd_start(message):
    # Dar la bienvenida al usuario del bot
    bot.send_chat_action(message.chat.id, "typing")
    # Mostrar un mensaje con botones inline, debajo del mensaje
    markup = InlineKeyboardMarkup(row_width=1)  # Numero de botones por fila (3 por defecto)
    # Botones
    b1 = InlineKeyboardButton("Start", callback_data="start")
    b2 = InlineKeyboardButton("Info", callback_data="info")
    b3 = InlineKeyboardButton("Help", callback_data="help")
    b4 = InlineKeyboardButton("Tienda", callback_data="tienda")

    markup.add(b1, b2, b3, b4)
    bot.reply_to(message,
                 "Hola Bienvenido a Tienda La Esperanza " + message.chat.first_name + ", aqui estan todos los comandos que puedes usar, para controlar "
                                                                                      "el bot.\n\n/start - Mostrar todos los comandos\n\n/buttons - Te "
                                                                                      "muestra los botones para realizar las consultas\n\n/info - "
                                                                                      "Ofrece informacion sobre el bot\n\n/help - Te dara una pequeña "
                                                                                      "descripcion de como puedes interactuar con el bot\n\n/tienda - Acesso a la tienda",
                 reply_markup=markup)
    # cmd_button_comman(message)


# Responde al comando info
@bot.message_handler(commands=["info"])
def cmd_info(message):
    # Ofrece informacion sobre el bot y su autor
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


@bot.message_handler(commands=["tienda"])
def cmd_tienda(message):
    # Ofrece ayuda sobre como utilizar el bot
    bot.send_chat_action(message.chat.id, "typing")
    # Mostrar un mensaje con botones inline, debajo del mensaje
    markup = InlineKeyboardMarkup(row_width=2)  # Numero de botones por fila (3 por defecto)
    # Botones
    b1 = InlineKeyboardButton("Login", callback_data="login")
    b2 = InlineKeyboardButton("Registro", callback_data="reg")
    b3 = InlineKeyboardButton("cerrar", callback_data="exit")
    markup.add(b1, b2, b3)
    bot.send_message(message.chat.id, "Bienvenido a la Tienda antes de proseguir debe autenticarse:",
                     reply_markup=markup)


# Introduccion al escribir
greetings = ['Hola!! 🤠👋🏼', 'Buenos noches!! 🤓🌚', 'Hola!, que tal? 🧑🏻', 'Klk!! 🤣', 'Buenas tardes!! 😄🌞',
             'Saludos mi estimad@!! 😏👌🏼', 'Encantado de hablar contigo!! 😜', 'Saludos!! 😌', 'Guao tengo visita!! 😆',
             'Es agradable hablar con alguien!, tengo mucho tiempo solo 😔']


def cmd_button_comman(message):
    print(message)
    bot.send_chat_action(message.chat.id, "typing")
    # Mostrar un mensaje con botones inline, debajo del mensaje
    markup = InlineKeyboardMarkup(row_width=1)  # Numero de botones por fila (3 por defecto)
    # Botones
    b1 = InlineKeyboardButton("Start", callback_data="start")
    b2 = InlineKeyboardButton("Info", callback_data="info")
    b3 = InlineKeyboardButton("Help", callback_data="help")
    markup.add(b1, b2, b3)
    bot.reply_to(message,
                 "Hola Bienvenido a Tienda La Esperanza " + message.chat.first_name + ", aqui estan todos los comandos que puedes usar, para controlar "
                                                                                      "el bot.\n\n/start - Mostrar todos los comandos\n\n/buttons - Te "
                                                                                      "muestra los botones para realizar las consultas\n\n/info - "
                                                                                      "Ofrece informacion sobre el bot\n\n/help - Te dara una pequeña "
                                                                                      "descripcion de como puedes interactuar con el bot",
                 reply_markup=markup)
    bot.delete_message(message.chat.id, message.message_id)


# Responder a los mensajes sin poner comandos
# @bot.message_handler(content_types=["text"])
# def bot_mensajes_texto(message):
#     num = random.randint(0, 9)
#     # Gestiona los mensajes que recibe
#     # Esta funcion recibe dos parametros el chat id, tiene un identificador unico y el mensaje
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
    # Gestionara las acciones de los botones callback_data
    cid = call.from_user.id
    mid = call.message.id
    chat = call.message.chat.id
    message = call.message
    print(call.data)
    if call.data == "b1":
        botones_producto(cid, mid, chat)
    elif call.data == 'b3':
        cmd_button_orden_estado(chat)
    elif call.data == 'b4':
        cancelar_orden(message)
    elif call.data == 'b4':
        cmd_button_orden_estado(chat)
    elif call.data == 'esp':
        boton_esp(chat)
    elif call.data == 'reg':
        registro(chat)
    elif call.data == 'tienda':
        cmd_tienda(message)
    elif call.data == 'login':
        cmd_login(chat)
    elif call.data == '1' or call.data == '2' or call.data == '3' or call.data == '4' or call.data == '5' or call.data == '6':
        buscar_estados(call)
    elif call.data == 'col':
        respuesta_botones_de_producto_buscar_color(call)
        bot.send_message(call.message.chat.id, 'Elija una Opcion?')
    elif call.data == 'col':
        respuesta_botones_de_producto_buscar_color(call)
        bot.send_message(call.message.chat.id, 'Elija una Opcion?')
    elif call.data == 'tam':
        respuesta_botones_de_producto_buscar_size(chat)
    elif call.data == 'pe':
        respuesta_botones_de_producto_buscar_weigth(chat)
    elif call.data == 'cat':
        respuesta_botones_de_producto_buscar_categoria(chat)
    elif call.data == 'nom':
        respuesta_botones_de_producto_buscar_nombre(chat)
    elif call.data == 'num':
        respuesta_botones_de_producto_buscar_num(chat)


def registro(chat):
    markup = ForceReply()  # Numero de botones por fila (3 por defecto)
    msg = bot.send_message(chat, "Digite un  Nombre de Usuario:", reply_markup=markup)
    bot.register_next_step_handler(msg, cmd_regist_username)


def regi_password(chat):
    markup = ForceReply()  # Numero de botones por fila (3 por defecto)
    msg = bot.send_message(chat, "Digite un  Password:", reply_markup=markup)
    bot.register_next_step_handler(msg, cmd_regist_password)
def regi_email(chat):
    markup = ForceReply()  # Numero de botones por fila (3 por defecto)
    msg = bot.send_message(chat, "Digite un  email:", reply_markup=markup)
    bot.register_next_step_handler(msg, cmd_regist_email)

def cancelar_orden(message):
    markup = InlineKeyboardMarkup(row_width=2)
    si = InlineKeyboardButton(text='SI', callback_data='S')
    no = InlineKeyboardButton(text='NO', callback_data='n')
    cerrar = InlineKeyboardButton(text='Cerrar', callback_data='exit')
    markup.add(si, no, cerrar)
    bot.send_message(message.chat.id, "Esta seguro Que desea Cancelar la orden?", reply_markup=markup)


def buscar_estados(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)
    markup.add('Buscar', 'volver al menu')
    estado = message.data
    print(estado)
    print(usuarios[message.message.chat.id]['id'])
    productos = estado_orden(usuarios[message.message.chat.id]['id'], estado)

    if bool(productos):
        for producto in productos:
            texto = f'Orden #:<code>{producto[0]}</code>\n\n '
            texto += f'<code>Direccion de Envio: </code>{producto[1]}\n'
            texto += f'<code>Metodo de Envio: </code>{producto[2]}\n'
            texto += f'<code>Sub Total: </code>{producto[3]}\n'
            texto += f'<code>Impuesto: </code>{producto[4]}$\n'
            texto += f'<code>Cargo de envio: </code>{producto[5]}\n'
            texto += f'<code>Monto Total: </code>{producto[6]}\n'

            bot.send_message(message.message.chat.id, texto, parse_mode='html')
        msg = bot.send_message(message.message.chat.id, 'Desea seguir Buscando?', reply_markup=markup)
        bot.register_next_step_handler(msg, cmd_button_orden_estado)
    else:
        bot.send_message(message.message.chat.id, 'No se encontraron resultados para esta consulta')
        msg = bot.send_message(message.message.chat.id, 'Desea seguir Buscando?', reply_markup=markup)
        bot.register_next_step_handler(msg, cmd_button_orden_estado)


def cmd_login(chat):
    markup = ForceReply()  # Numero de botones por fila (3 por defecto)
    msg = bot.send_message(chat, "Cual es su Nombre de Usuario:", reply_markup=markup)
    bot.register_next_step_handler(msg, cmd_buscar_username)


def cmd_login_2(chat):
    markup = ForceReply()  # Numero de botones por fila (3 por defecto)
    msg = bot.send_message(chat, "Cual es su Password:", reply_markup=markup)
    bot.register_next_step_handler(msg, cmd_entrar)


def cmd_entrar(message):
    text = message.text
    name = usuarios[message.chat.id]['username']
    print(name)
    resp = login(name, text)
    chat = message.chat.id
    print(resp[0][4])
    if bool(resp):
        usuarios[message.chat.id] = {}
        usuarios[message.chat.id]['pass'] = message.text
        usuarios[message.chat.id]['email'] = resp[0][3]
        usuarios[message.chat.id]['id'] = resp[0][4]
        cmd_button(message)

    else:
        markup = ForceReply()
        msg = bot.send_message(chat, "Password incorrecto: digitelo de nuevo", reply_markup=markup)
        bot.register_next_step_handler(msg, cmd_entrar)


def cmd_regist_username(message):
    text = message.text
    chat = message.chat.id
    if bool(text):
        usuario[message.chat.id] = {}
        usuario[message.chat.id]['username'] = message.text
        regi_password(chat)
    else:
        markup = ForceReply()
        msg = bot.send_message(chat, "Este Usuario  existe en la Base de datos: digitelo de nuevo",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, registro)


def cmd_regist_password(message):
    text = message.text
    chat = message.chat.id
    if bool(text):
        usuario[message.chat.id]['password'] = message.text
        regi_email(chat)
    else:
        markup = ForceReply()
        msg = bot.send_message(chat, "Password invalido: digitelo de nuevo",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, cmd_regist_password)

def cmd_regist_email(message):
    text = message.text
    id=random.randint(1,1000)
    chat = message.chat.id
    if bool(text):
        usuario[message.chat.id]['email'] = message.text
        usuario[message.chat.id]['id'] = id
        registrar_user(message)

    else:
        markup = ForceReply()
        msg = bot.send_message(chat, "Password invalido: digitelo de nuevo",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, cmd_regist_password)
def registrar_user(message):
    print(usuario)
    user=usuario[message.chat.id]['username']
    password=usuario[message.chat.id]['password']
    email=usuario[message.chat.id]['email']
    id=usuario[message.chat.id]['id']
    resp = registrar_usuario_nuevo(user,password,email,id)
    print(resp)
    if bool(resp):
        print( bool(resp))
        usuario[message.chat.id] = {}
        usuario[message.chat.id]['email'] = message.text
        usuario[message.chat.id]['id'] = id
        cmd_tienda(message)

    else:

        msg = bot.send_message(message.chat.id, "Error al registrar el usuario")
        bot.register_next_step_handler(msg, cmd_tienda)

def cmd_buscar_username(message):
    text = message.text
    resp = traer_username(text)
    chat = message.chat.id
    if bool(resp):
        usuarios[message.chat.id] = {}
        usuarios[message.chat.id]['username'] = message.text
        cmd_login_2(chat)
    else:
        markup = ForceReply()
        msg = bot.send_message(chat, "Este Usuario no existe en la Base de datos: digitelo de nuevo",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, cmd_buscar_username)


@bot.callback_query_handler(func=lambda call: True)
def respuesta_botones_de_producto_buscar(call):
    # Gestionara las acciones de los botones callback_data
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
    if call.data == "col":
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

    if bool(productos):
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
        bot.register_next_step_handler(msg, volver_a_preguntar)
    else:
        bot.send_message(message.chat.id, 'No se encontraron resultados para esta consulta')
        msg = bot.send_message(message.chat.id, 'Desea seguir Buscando?', reply_markup=markup)
        bot.register_next_step_handler(msg, volver_a_preguntar)


def volver_a_preguntar(message):
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
    if bool(productos):
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
    else:
        bot.send_message(message.chat.id, 'No se encontraron resultados para esta consulta')
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
    bot.register_next_step_handler(msg, producto_buscar_weigth)


def producto_buscar_weigth(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)
    markup.add('Buscar', 'volver al menu')
    size = message.text
    productos = traer_productos_por_weight(size)
    if bool(productos):
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

    else:
        bot.send_message(message.chat.id, 'No se encontraron resultados para esta consulta')
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
    markup = InlineKeyboardMarkup(row_width=1)  # Numero de botones por fila (3 por defecto)
    # Botones
    b1 = InlineKeyboardButton("color del Producto", callback_data="col")
    b2 = InlineKeyboardButton("Tamaño del  PRODUCTOS", callback_data="tam")
    b3 = InlineKeyboardButton("Peso del Producto", callback_data="pe")
    markup.add(b1, b2, b3)
    bot.send_message(chat, "Puede Consultar sus productos por la siguiente Opciones", reply_markup=markup)


def respuesta_botones_de_producto_buscar_categoria(chat):
    # Gestionara las acciones de los botones callback_data

    print(min)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)  # Numero de botones por fila (3 por defecto)
    markup.add('Accessories', 'Bib-Shorts',
               'Bike Racks',
               'Bike Stands',
               'Bikes',
               'Bottles and Cages',
               'Bottom Brackets',
               'Brakes',
               'Caps',
               'Chains',
               'Cleaners',
               'Clothing',
               'Components',
               'Cranksets',
               'Derailleurs',
               'Fenders',
               'Forks',
               'Gloves',
               'Handlebars',
               'Headsets',
               'Helmets',
               'Hydration Packs',
               'Jerseys',
               'Lights',
               'Locks',
               'Mountain Bikes',
               'Mountain Frames',
               'Panniers',
               'Pedals',
               'Pumps',
               'Road Bikes',
               'Road Frames',
               'Saddles',
               'Shorts',
               'Socks',
               'Tights',
               'Tires and Tubes',
               'Touring Bikes',
               'Touring Frames',
               'Vests',
               'Wheels')
    msg = bot.send_message(chat, "Elija una Categoria:\n\n", reply_markup=markup)
    bot.register_next_step_handler(msg, producto_buscar_categoria)


def producto_buscar_categoria(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)
    markup.add('Buscar', 'volver al menu')
    cat = message.text
    print(cat)
    productos = traer_productos_por_categoria(cat)
    if bool(productos):
        for producto in productos:
            texto = 'Detalles de Productos:\n\n '
            texto += f'<code>Numero del producto: </code>{producto[0]}\n'
            texto += f'<code>Nombre del producto: </code>{producto[1]}\n'
            texto += f'<code>Color del producto: </code>{producto[2]}\n'
            texto += f'<code>Precio del producto: </code>{producto[3]}$\n'
            texto += f'<code>Tamaño del producto: </code>{producto[4]}\n'
            texto += f'<code>Categoria del producto: </code>{producto[6]}\n'
            bot.send_message(message.chat.id, texto, parse_mode='html')
        msg = bot.send_message(message.chat.id, 'Desea seguir Buscando?', reply_markup=markup)
        bot.register_next_step_handler(msg, volver_a_preguntar_cat)
    else:
        bot.send_message(message.chat.id, 'No se encontraron resultados para esta consulta')
        msg = bot.send_message(message.chat.id, 'Desea seguir Buscando?', reply_markup=markup)
        bot.register_next_step_handler(msg, volver_a_preguntar_cat)


def volver_a_preguntar_cat(message):
    cid = message.from_user.id
    mid = message.id
    chat = message.chat.id
    if message.text == 'Buscar':
        respuesta_botones_de_producto_buscar_categoria(chat)

    else:
        cid = message.from_user.id
        mid = message.id
        chat = message.chat.id
        botones_producto(cid, mid, chat)


def respuesta_botones_de_producto_buscar_nombre(chat):
    # Gestionará las acciones de los botones callback_data
    print(min)
    markup = ForceReply()  # Número de botones por fila (3 por defecto)
    msg = bot.send_message(chat, 'Digite el nombre del producto:'
                                 "", reply_markup=markup)
    bot.register_next_step_handler(msg, producto_buscar_nombre)


def producto_buscar_nombre(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)
    markup.add('Buscar', 'volver al menu')
    cat = message.text
    print(cat)
    productos = traer_productos_por_nombre(cat)
    if bool(productos):
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
        bot.register_next_step_handler(msg, volver_a_preguntar_nombre)
    else:
        bot.send_message(message.chat.id, 'No se encontraron resultados para esta consulta')
        msg = bot.send_message(message.chat.id, 'Desea seguir Buscando?', reply_markup=markup)
        bot.register_next_step_handler(msg, volver_a_preguntar_nombre)


def volver_a_preguntar_nombre(message):
    cid = message.from_user.id
    mid = message.id
    chat = message.chat.id
    if message.text == 'Buscar':
        respuesta_botones_de_producto_buscar_nombre(chat)

    else:
        cid = message.from_user.id
        mid = message.id
        chat = message.chat.id
        botones_producto(cid, mid, chat)


def respuesta_botones_de_producto_buscar_num(chat):
    # Gestionará las acciones de los botones callback_data
    print(min)
    markup = ForceReply()  # Número de botones por fila (3 por defecto)
    msg = bot.send_message(chat, 'Digite el numero del producto:'
                                 "", reply_markup=markup)
    bot.register_next_step_handler(msg, producto_buscar_num)


def producto_buscar_num(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)
    markup.add('Buscar', 'volver al menu')
    cat = message.text
    print(cat)
    productos = traer_productos_por_num(cat)
    if bool(productos):
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
        bot.register_next_step_handler(msg, volver_a_preguntar_num)
    else:
        bot.send_message(message.chat.id, 'No se encontraron resultados para esta consulta')
        msg = bot.send_message(message.chat.id, 'Desea seguir Buscando?', reply_markup=markup)
        bot.register_next_step_handler(msg, volver_a_preguntar_num)


def volver_a_preguntar_num(message):
    cid = message.from_user.id
    mid = message.id
    chat = message.chat.id
    if message.text == 'Buscar':
        respuesta_botones_de_producto_buscar_num(chat)

    else:
        cid = message.from_user.id
        mid = message.id
        chat = message.chat.id
        botones_producto(cid, mid, chat)


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
                     "Bienvenido a Tienda  La Esperanza Bot,\n Soy su asistente virtual es un gusto tenerte por "
                     "aqui!!.\n\nTienda La Esperanza es un bot creado para facilitar "
                     "consultas, compras y reservas de nuestros productos disponibles. Si buscas mas informacion "
                     "digite /start")

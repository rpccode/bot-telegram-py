
from db import *
from config import *  # importamos el token
import telebot
import asyncio
import time
import random
import threading
import asyncio
from decimal import Decimal
# Botones inline
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, LabeledPrice,ShippingOption  # Crea botones inline
from telebot.types import ReplyKeyboardMarkup, ForceReply, ReplyKeyboardRemove  # Define los botones inline



bot = telebot.TeleBot(TOKEN2)
bot.set_webhook()

usuarios = {}
usuario = {}
lista_articulos = {}
list_a = list()



shipping_options = [
    ShippingOption(id='instant', title='WorldWide Teleporter').add_price(LabeledPrice('Teleporter', 1000)),
    ShippingOption(id='pickup', title='Local pickup').add_price(LabeledPrice('Pickup', 300))]


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
    b5 = InlineKeyboardButton("Carra de Producto", callback_data="b5")
    markup.add(b1, b2, b3, b4, b5)
    bot.send_message(message.chat.id, "Tiendas BiciCentro", reply_markup=markup)


def cmd_button_orden_estado(message):
    bot.send_chat_action(message.chat.id, "typing")
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
    bot.send_message(message.chat.id, "Verifica el Estado de tu reserva:", reply_markup=markup)


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
                 "Hola Bienvenido a Tiendas BiciCentro " + message.chat.first_name +
                 ", aqui estan todos los comandos que puedes usar, para controlar "
                 "el bot.\n\n/start - Mostrar todos los comandos\n\n/buttons - Te "
                 "muestra los botones para realizar las consultas\n\n/info - "
                 "Ofrece informacion sobre el bot\n\n/help - Te dara una pequeña "
                 "descripcion de como puedes interactuar con la tienda.\n\n/Acesso a la tienda",
                 reply_markup=markup)
    # cmd_button_comman(message)


# Responde al comando info
@bot.message_handler(commands=["info"])
def cmd_info(message):
    # Ofrece informacion sobre el bot y su autor
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message,
                 "Hola " + message.chat.first_name + ", aqui esta la informacion sobre tiendas BiciCentro.\n\n")
    # Messages
    bot.send_message(
        message.chat.id, "DIRECCION.\n Av. Juan Pablo Duarte casi esq. Benito Juarez Edificio Alejo, Villa Olga.")
    bot.send_message(
        message.chat.id, "CORREO ELECTRONICO.\n: bicicentro@gmail.com")
    bot.send_message(message.chat.id,
                     "HORARIOS\n\nDomingo\tNo laborable\nLunes\t\t\t08:00:00AM - "
                     "10:00:00PM\nMartes\t\t\t08:00:00AM - 10:00:00PM\nMiercoles\t\t\t08:00:00AM - "
                     "10:00:00PM\nJueves\t\t\t08:00:00AM - 10:00:00PM\nViernes\t\t\t08:00:00AM - "
                     "10:00:00PM\nSabado\t\t\t08:00:00AM - 12:00:00PM\n")
    bot.send_message(message.chat.id,
                     "TELEFONOS\n\nTelefonos disponibles:\n\nTelefono #1: (809) 582-4146\nTelefono #2: (809) "
                     "575-6000\nTelefono #3: (809) 241-6262\n")
    bot.send_message(message.chat.id, "[PAGINA WEB](https://bicicentro.com.do/)", parse_mode="MarkDownV2",
                     disable_web_page_preview=True)
    bot.send_message(message.chat.id,
                     "[FACEBOOK](https://web.facebook.com/bicicentroenlinea/?_rdc=1&_rdr)",
                     parse_mode="MarkDownV2", disable_web_page_preview=True)
    bot.send_message(message.chat.id, "[GMAIL](https://mail.google.com/mail/u/0/?tab=rm&ogbl)", parse_mode="MarkDownV2",
                     disable_web_page_preview=True)


# Responden al comando help
@bot.message_handler(commands=["help"])
def cmd_help(message):
    # Ofrece ayuda sobre como utilizar el bot
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message,
                 "Hola este es el apartado de ayuda: Digitar los siguientes comandos en el chat\n\nPara poder "
                 "contactar con el bot puedes utilizar el comando /start.\nPara ver los botones disponibles "
                 "/buttons.\nPara ver informacion detallada sobre tiendas BiciCentro /info.\n Verificar "
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
    bot.send_message(message.chat.id, "Bienvenido a tiendas BiciCentro antes de proseguir debe autenticarse:",
                     reply_markup=markup)


# Introduccion al escribir
greetings = ['Hola!! 🤠👋🏼', 'Buenos noches!! 🤓🌚', 'Hola!, que tal? 🧑🏻', 'Klk!! 🤣', 'Buenas tardes!! 😄🌞',
             'Saludos mi estimad@!! 😏👌🏼', 'Encantado de hablar contigo!! 😜', 'Saludos!! 😌', 'Guao tengo visita!! 😆',
             'Es agradable hablar con alguien!, tengo mucho tiempo solo 😔']


def cmd_button_comman(message):

    bot.send_chat_action(message.chat.id, "typing")
    # Mostrar un mensaje con botones inline, debajo del mensaje
    markup = InlineKeyboardMarkup(row_width=1)  # Numero de botones por fila (3 por defecto)
    # Botones
    b1 = InlineKeyboardButton("Start", callback_data="start")
    b2 = InlineKeyboardButton("Info", callback_data="info")
    b3 = InlineKeyboardButton("Help", callback_data="help")
    markup.add(b1, b2, b3)
    bot.reply_to(message,
                 "Hola Bienvenido a tiendas BiciCentro " + message.chat.first_name +
                 ", aqui estan todos los comandos que puedes usar, para controlar "
                 "el bot.\n\n/start - Mostrar todos los comandos\n\n/buttons - Te "
                 "muestra los botones para realizar las consultas\n\n/info - "
                 "Ofrece informacion sobre el bot\n\n/help - Te dara una pequeña "
                 "descripcion de como puedes interactuar.",
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
#     if message.text == 'Menu':
#         cmd_button(message)
#     elif message.text == 'Reserva':
#         cmd_button()

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
        cmd_button_orden_estado(message)
    elif call.data == 'b2':
        cmd_agregar_articulo(message)
    elif call.data == 'b4':
        cancelar_orden(message)
    elif call.data == 'b5':
        ver_lista(message)
    elif call.data == 'pa':
       command_pay(message)
    elif call.data == 'can':
        bot.delete_message(cid, mid)
        cmd_button(message)
    elif call.data == 'esp':
        boton_esp(chat)
    elif call.data == 'reg':
        registro(chat)
    elif call.data == 'tienda':
        cmd_tienda(message)
    elif call.data == 'start':
        cmd_start(message)
    elif call.data == 'help':
        cmd_help(message)
    elif call.data == 'info':
        cmd_info(message)
    elif call.data == 'login':
        cmd_login(chat)
    elif call.data == 'S':
        cancelar_ordenes(chat)
    elif call.data == 'n':
        cmd_button(message)
    elif call.data == '1' or call.data == '2' or call.data == '3' or call.data == '4' or call.data == '5' or call.data == '6':
        buscar_estados(call)
    elif call.data == 'col':
        respuesta_botones_de_producto_buscar_color(call)
        bot.send_message(call.message.chat.id, 'Elija una Opcion?')
    elif call.data == 'pre':
        respuesta_botones_de_producto_buscar_precio(call)
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


def cancelar_ordenes(chat):
    markup = ForceReply()  # Numero de botones por fila (3 por defecto)
    msg = bot.send_message(chat, "Digite un  Nombre de Orden a Cancelar:", reply_markup=markup)
    bot.register_next_step_handler(msg, db_cancela_orden)


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


def db_cancela_orden(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)
    markup.add('Buscar', 'volver al menu')
    num = message.text
    resl = Cancel_orden(num, usuarios[message.chat.id]['email'])

    if resl == 1:
        bot.send_message(message.chat.id, 'Orden Cancelada')
        msg = bot.send_message(message.chat.id, 'Desea seguir Cancelando?', reply_markup=markup)
        bot.register_next_step_handler(msg, cmd_button)
    else:
        bot.send_message(message.chat.id, 'Error al Cancelar la orden ')
        msg = bot.send_message(message.chat.id, 'Desea seguir Buscando?', reply_markup=markup)
        bot.register_next_step_handler(msg, cmd_button)


def buscar_estados(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)
    markup.add('Buscar', 'volver al menu')
    estado = message.data

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
    id = random.randint(1, 1000)
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
    user = usuario[message.chat.id]['username']
    password = usuario[message.chat.id]['password']
    email = usuario[message.chat.id]['email']
    id = usuario[message.chat.id]['id']
    resp = registrar_usuario_nuevo(user, password, email, id)
    print(resp)
    if bool(resp):
        print(bool(resp))
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


def respuesta_botones_de_producto_buscar_precio(call):
    # Gestionara las acciones de los botones callback_data
    cid = call.from_user.id
    mid = call.message.id
    chat = call.message.chat.id
    print(min)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)  # Numero de botones por fila (3 por defecto)
    markup.add('0 a 100', '100 a 500', '500 a 1000', '1000 a 1500', '1500 a 2000', '2000 a 2500')
    msg = bot.send_message(chat, "Para facilitar su Busqueda puede elejir una de las siguientes opciones:\n\n ",
                           reply_markup=markup)
    bot.register_next_step_handler(msg, producto_buscar_precio)


def producto_buscar_precio(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)
    markup.add('Buscar', 'volver al menu')
    color = message.text
    if color == '0 a 100':
        productos = traer_productos_por_precio(0, 100)
    elif color == '100 a 500':
        productos = traer_productos_por_precio(100, 500)
    elif color == '500 a 1000':
        productos = traer_productos_por_precio(500, 1000)
    elif color == '1000 a 1500':
        productos = traer_productos_por_precio(1000, 1500)
    elif color == '1500 a 2000':
        productos = traer_productos_por_precio(1500, 2000)
    elif color == '2000 a 2500':
        productos = traer_productos_por_precio(2000, 2500)

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
        bot.register_next_step_handler(msg, volver_a_preguntar_precio)
    else:
        bot.send_message(message.chat.id, 'No se encontraron resultados para esta consulta')
        msg = bot.send_message(message.chat.id, 'Desea seguir Buscando?', reply_markup=markup)
        bot.register_next_step_handler(msg, volver_a_preguntar_precio)


def volver_a_preguntar_precio(message):
    cid = message.from_user.id
    mid = message.id
    if message.text == 'Buscar':
        bot.delete_message(message.chat.id, message.message_id)
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                     row_width=3)  # Numero de botones por fila (3 por defecto)
        markup.add('0 a 100', '100 a 500', '500 a 1000', '1000 a 1500', '1500 a 2000', '2000 a 2500')
        msg = bot.send_message(message.chat.id,
                               "Para facilitar su Busqueda puede elejir una de las siguientes opciones:\n\n ",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, producto_buscar_precio)


    else:
        cid = message.from_user.id
        mid = message.id
        chat = message.chat.id
        botones_producto(cid, mid, chat)


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


def cmd_agregar_articulo(message):
    markup = ForceReply()  # Numero de botones por fila (3 por defecto)
    bot.send_message(message.chat.id, 'Favor de agregar tus artículos')
    msg = bot.send_message(message.chat.id, "Numero de Producto:", reply_markup=markup)
    bot.register_next_step_handler(msg, agregar_articulos)


# funcion para agregar articulos a nuestra listaa
def agregar_articulos(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)
    markup.add('Buscar', 'volver al menu')
    text = message.text
    produt = traer_productos_por_num1(text)
    if bool(produt):

        lista_articulos[message.chat.id]['num'] = produt[0][2]
        lista_articulos[message.chat.id]['nom'] = produt[0][1]
        lista_articulos[message.chat.id]['col'] = produt[0][3]
        lista_articulos[message.chat.id]['prec'] = produt[0][5]
        lista_articulos[message.chat.id]['tam'] = produt[0][6]
        lista_articulos[message.chat.id]['anch'] = produt[0][7]
        list_a.append(lista_articulos[message.chat.id])

        bot.send_message(message.chat.id, "Articulo agregado")
        msg = bot.send_message(message.chat.id, "Desea seguir Buscando?:", reply_markup=markup)
        bot.register_next_step_handler(msg, volver_a_preguntar_num1)
    else:
        # bot.send_message(message.chat.id, 'No se encontro El articulo,\n\n Por favor  Digite otro')
        msg = bot.send_message(message.chat.id, 'No se encontro El articulo,\n\n Por favor  Digite otro',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, volver_a_preguntar_num1)


def volver_a_preguntar_num1(message):
    cid = message.from_user.id
    mid = message.id
    chat = message.chat.id
    if message.text == 'Buscar':
        cmd_agregar_articulo(message)

    else:
        cid = message.from_user.id
        mid = message.id
        chat = message.chat.id
        cmd_button(message)


# Funcion para borrar elementos de nuestra lista
def borrar_articulos(message):
    articulo = input("Elementos a eliminar: ")
    # Agregamos de nuevo string.capitaliza()para que python no marque error
    lista_articulos.remove(articulo.capitalize())
    print("El articulo se ha borrado con exito!")


# Funcion para imprimir los artculos de nuestra lista
def ver_lista(message):
    global reserva
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 row_width=3)
    markup.add('Buscar', 'Menu', 'Reservar')
    # muestra los articulos en forma de lista de python
    # print(lista_articulos)
    bot.send_message(message.chat.id, "-------- Articulos en tu Carrito  ------------")

    i = 0
    prec = 0
    porcent = Decimal(0.30)
    for articulos in list_a:
        i += 1
        texto = f'Productos #: {i}\n\n '
        texto += f'<code>Numero del producto: </code>{articulos["num"]}\n'
        texto += f'<code>Nombre del producto: </code>{articulos["nom"]}\n'
        texto += f'<code>Color del producto: </code>{articulos["col"]}\n'
        texto += f'<code>Precio del producto: </code>${round(articulos["prec"])} USD\n'
        texto += f'<code>Tamaño del producto: </code>{articulos["tam"]}\n'
        texto += f'<code>Ancho del producto: </code>{articulos["anch"]} cm\n\n'
        prec += articulos["prec"]
        bot.send_message(message.chat.id, f"------------------\n\n  {texto} \n\n ---------------- ", parse_mode='html')

    reserva = round((prec * porcent))
    msg = bot.send_message(message.chat.id, f"Estos son tus articulos\n\n"
                                            f"Cantida de articulos: {i}\n"
                                            f"Total a pagar para reservar: ${reserva} USD", reply_markup=markup)
    bot.register_next_step_handler(msg, volver_a_preguntar_carrito)


def pagar_reserva(message):
    cid = message.from_user.id
    mid = message.id
    chat = message.chat.id
    markup = InlineKeyboardMarkup(row_width=1)  # Numero de botones por fila (3 por defecto)
    # Botones
    b1 = InlineKeyboardButton("Pagar", callback_data="pa")
    b2 = InlineKeyboardButton("Cancelar", callback_data="can")
    markup.add(b1, b2)
    bot.send_message(chat, f"Total a Pagar para Reservar:\t{reserva} USD",
                     reply_markup=markup)


def volver_a_preguntar_carrito(message):
    cid = message.from_user.id
    mid = message.id
    chat = message.chat.id
    if message.text == 'Buscar':
        cmd_agregar_articulo(message)

    elif message.text == 'Reservar':
        pagar_reserva(message)
    else:
        cid = message.from_user.id
        mid = message.id
        chat = message.chat.id
        cmd_button(message)


@bot.message_handler(commands=['buy'])
def command_pay(message):
    prices =[LabeledPrice(label='Reserva', amount=(reserva*100)), LabeledPrice('Tax', 500)]
    bot.send_invoice(
        message.chat.id,  # chat_id
        'Reservar Productos',  # title
        'Paga y Reserva tus Productos ahora!',
        # description
        'HAPPY FRIDAYS COUPON',  # invoice_payload
        provider_token,  # provider_token
        'usd',  # currency
        prices,  # prices
        photo_url='https://www.kindpng.com/picc/m/47-479448_payment-method-payments-icon-hd-png-download.png',
        photo_height=312,  # !=0/None or picture won't be shown
        photo_width=412,
        photo_size=412,
        is_flexible=False,  # True If you need to set up Shipping Fee
        start_parameter='time-machine-example')


@bot.shipping_query_handler(func=lambda query: True)
def shipping(shipping_query):
    print(shipping_query)
    bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options,
                              error_message='Oh, seems like our Dog couriers are having a lunch right now. Try again later!')


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Aliens tried to steal your card's CVV, but we successfully protected your credentials,"
                                                " try to pay again in a few minutes, we need a small rest.")


@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    bot.send_message(message.chat.id,
                     '¡Hurra! ¡Gracias por el pago! ¡Procederemos con su pedido por `{} {}` lo más rápido posible! '
                     'Verificaremos su solicitud y Nos Mantendremos en Conctacto con  ustep en breve!'.format(
                         message.successful_payment.total_amount / 100, message.successful_payment.currency),
                     parse_mode='Markdown')
    cmd_button(message)

if __name__ == '__main__':
    print("Bot iniciando...")
    # Configurar los comandos de nuestro bot
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Te muestra todos los comandos disponibles"),
        telebot.types.BotCommand("/buttons", "Te muestra los botones para realizar las consultas"),
        telebot.types.BotCommand("/info", "Ofrece informacion sobre el bot"),
        telebot.types.BotCommand("/help", "Ofrece ayuda sobre el bot"),
        telebot.types.BotCommand("/buy", "Ofrece ayuda sobre el bot")

    ])
    print("Bot en funcionamiento...")
    # Usando threading
    markup = ReplyKeyboardRemove()
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    lista_articulos[MI_CHAT_ID] = {}
    foto = open("./public/images/bicicentro.jpg", "rb")
    bot.send_photo(MI_CHAT_ID, foto, "Tiendas BiciCentro")
    bot.send_message(MI_CHAT_ID,
                     "Bienvenido a tiendas BiciCentro,\n Soy su asistente virtual es un gusto tenerte por "
                     "aqui!!.\n\nTiendas BiciCentro es un bot creado para facilitar "
                     "consultas, compras y reservas de nuestros productos disponibles. Si buscas mas informacion "
                     "digite /start")
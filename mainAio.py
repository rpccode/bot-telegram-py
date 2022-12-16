from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
from data import *

bot = Bot(token='5926816130:AAF0YddnlJ64rj4OxpX3VtT-0BNIA_TtN5A')
dp = Dispatcher(bot)


button1 = InlineKeyboardButton(
    text="ℹ   button1", callback_data="randomvalue_of10")
button2 = InlineKeyboardButton(
    text="🔍 button2", callback_data="randomvalue_of100")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)

keyboard1 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("ℹ  Informacion", "🔍Consulta")

keyboard2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("🧭 Horarios", "🚹  Servicios")

keyboard3 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("ℹ Productos", "🔍Orden")


@dp.message_handler(commands=['random'])
async def random_answer(message: types.Message):
    await message.reply("Hola! Este es el asistente virtual de Dart Tienda\n ¿En que puedo ayudarle?:", reply_markup=keyboard_inline)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hola! Este es el asistente virtual de Dart Tienda\n ¿En que puedo ayudarle?", reply_markup=keyboard1)


@dp.callback_query_handler(text=["randomvalue_of10", "randomvalue_of100"])
async def random_value(call: types.CallbackQuery):
    if call.data == "randomvalue_of10":
        await call.message.reply("'ℹ  Informacion ", reply_markup=keyboard1)
    if call.data == "randomvalue_of100":
        await call.message.answer(randint(1, 100))
    await call.answer()


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == 'ℹ  Informacion':
        await message.reply("Que Informacion Nesecita?", reply_markup=keyboard2
                            )
    elif message.text == '🔍Consulta':
        await message.reply("Que desea consultar?", reply_markup=keyboard3)
    else:
        await message.reply(f"Your message is: {message.text}")


@dp.message_handler()
async def kb_answer2(message: types.Message):
    if message.text == '🧭 Horarios':
        await message.reply("Hi! How are you {  }")
    elif message.text == '🚹  Servicios':
        await message.reply("https://youtube.com/gunthersuper")
    else:
        await message.reply(f"Your message is: {message.text}")


@dp.message_handler()
async def kb_answer3(message: types.Message):
    if message.text == 'ℹ Productos':
        await message.reply(f"Hi! How are you? { datos()  }")
    elif message.text == '🔍Orden':
        await message.reply("https://youtube.com/gunthersuper")
    else:
        await message.reply(f"Your message is: { datos() }")


executor.start_polling(dp)

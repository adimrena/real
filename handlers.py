from kb import *
from aiogram import types
from aiogram import asyncio
from aiogram.types import Message, CallbackQuery, MediaGroup, InputFile, LabeledPrice, PreCheckoutQuery
from aiogram.dispatcher.filters import Command
from aiogram.types.message import ContentType
from kb import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from datetime import datetime, timedelta, timezone
import random
import aiogram.utils.markdown as md
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, MediaGroup
from aiogram.types import InputMediaDocument
from config import *
from main import dp,bot
import pandas as pd


import sqlite3



class Form(StatesGroup):
    record  = State()

@dp.message_handler(Command('start'))
async def start(message: Message):
    await message.answer(f"Привет, {message.chat.first_name}👋\nЯ - бот команды N.ERA - <b>специалистов</b> недвижимости в Дубае.\nБлагодаря глубокому знанию <b>конъюнктуры зарубежного рынка</b> и <b>тщательной оценке</b> экономических и правовых аспектов, мы помогаем подобрать <b>квартиру</b> как для <b>жизни</b>, так и для <b>инвестиций</b>.\n\nС моей помощью ты сможешь:\n\n🌴Получить гайд\n\n🌴записаться на консультацию\n\n🌴подобрать для себя квартиру в Дубае""", reply_markup=fkb)
    connect = sqlite3.connect('rena.db')
    cursor = connect.cursor()
    if cursor.execute("SELECT * FROM users WHERE user_id = ?", (message.chat.id,)).fetchone() == None:
        cursor.execute("INSERT INTO users (user_id, name, user_name) VALUES (?, ?, ?)", [message.chat.id, message.chat.first_name,message.from_user.username ])
        cursor.close()
        connect.commit()
        connect.close()
    else:
        cursor.close()
        connect.commit()
        connect.close()


@dp.callback_query_handler(text= 'cons')
async def l1(call:types.callback_query):
    await Form.record.set()
    await call.message.edit_text('<b>Напишите удобные для Вас дату, время и способ связи, чтобы мы могли связаться с вами</b>')
    

@dp.message_handler(state=Form.record)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['record'] = message.text
    await bot.forward_message(732659141, message.from_user.id, message.message_id)
    await bot.send_message(732659141,data['record']+'\nusername = @'+str(message.from_user.username))
    await bot.send_message(message.chat.id,'Ваша запись доставлена!\n\nСкоро наш специалист с вами свяжется!',reply_markup=tkb)
    await state.finish()


@dp.callback_query_handler(text= 'glav')
async def l1(call:types.callback_query):
    await call.message.edit_text(f"Привет, {call.message.chat.first_name}👋\nЯ - бот команды N.ERA - <b>специалистов</b> недвижимости в Дубае.\nБлагодаря глубокому знанию <b>конъюнктуры зарубежного рынка</b> и <b>тщательной оценке</b> экономических и правовых аспектов, мы помогаем подобрать <b>квартиру</b> как для <b>жизни</b>, так и для <b>инвестиций</b>.\n\nС моей помощью ты сможешь:\n\n🌴Получить гайд\n\n🌴записаться на консультацию\n\n🌴подобрать для себя квартиру в Дубае""", reply_markup=fkb)

@dp.callback_query_handler(text= 'guide')
async def l1(call:types.callback_query):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,'Подождите немного, гайд загружается')
    media = MediaGroup()
    media.attach(InputMediaDocument(open('guide.pdf', 'rb')))
    await bot.send_media_group(call.message.chat.id, media=media)
    await bot.send_message(call.message.chat.id,"В этом гайде я описала 2 основные <b>стратегии инвестирования</b> в недвижимость 🏡 Забирай к себе и пользуйся!", reply_markup=forkb)


@dp.callback_query_handler(text= 'podbor')
async def l1(call:types.callback_query):
    await Form.record.set()
    await call.message.edit_text('Напишите интересные для Вас объекты и районы в одном сообщении и удобные для Вас <b>дату, время и способ связи</b>, чтобы мы могли связаться с вами')


@dp.message_handler(Command('client'))
async def start(message: Message):
    connect = sqlite3.connect('rena.db')
    cursor = connect.cursor()
    df = pd.Series(cursor.execute("SELECT COUNT(user_id) FROM users"))
    await bot.send_message(message.chat.id,f"Всего пользователей в боте = {df[0]}")
    cursor.close()
    connect.commit()
    connect.close()

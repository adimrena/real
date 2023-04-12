from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

fkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('Получить гайд',callback_data='guide'),InlineKeyboardButton('Консультация',callback_data='cons'), InlineKeyboardButton('Подбор и разбор объекта', callback_data='podbor'))

skb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('Консультация',callback_data='cons'))

tkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('Главное меню',callback_data='glav'))

forkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('Запись на консультацию',callback_data='cons'),InlineKeyboardButton('Главное меню',callback_data='glav'))
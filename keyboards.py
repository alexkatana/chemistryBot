from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Таблица Менделеева')], [KeyboardButton(text = 'Таблица растворимости')]
], resize_keyboard=True,
input_field_placeholder='made by alexkatanaa')

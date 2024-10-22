
from aiogram import F, Router, types
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from bs4 import BeautifulSoup
import requests

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.reply(f'Привет, {message.from_user.first_name}! Я бот-помощник по химии. Введи или выбери нужный тебе элемент, и я моментально отправлю тебе нужную информацию о нем.',
                        reply_markup=kb.main)

@router.message(F.text == 'Таблица Менделеева')
async def Mendeleev(message: Message):
    await message.answer_photo('https://i.pinimg.com/originals/c0/5b/fc/c05bfcfb1d9b6804db3cb1262bb8c94e.gif', reply_markup=kb.main)

@router.message(F.text == 'Таблица растворимости')
async def Solubility(message: Message):
    await message.answer_photo('https://img.detmir.st/FmJ2w47MSPW-UQ3Atk22U8-A2NdT0D1YQz-guTqq2mc/rs:fit:2100:2100/g:sm/aHR0cHM6Ly9jYXRhbG9nLmRldG1pci5zdC9tZWRpYS9pMG9YQ2lwSTVPYXlSRzBOcE5DZDU3ZlY1ZTVjM1c0ZFV6aVAxT3ZLYVAwPQ.webp')

@router.message(F.text == 'тгк')
async def easter_egg(message: Message):
    await message.answer('https://t.me/vlxkvtvnv')


@router.message()
async def element(message: Message):

    text = message.text.replace(' ','_')
    url = f'https://ru.wikipedia.org/w/index.php?go=%D0%9F%D0%B5%D1%80%D0%B5%D0%B9%D1%82%D0%B8&search={text}'
    request = requests.get(url)
    
    search_soup = BeautifulSoup(request.text, 'html.parser')
    search_links = search_soup.find_all('div', class_='mw-search-result-heading')
    if len(search_links)>0:
        url = 'https://ru.wikipedia.org' + search_links[0].find('a')['href']

    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'lxml')
    try:
        table = []
        th_table = soup.find('tbody').find_all('th', class_='plainlist')
        tr_table = soup.find('tbody').find_all('td', class_='plainlist')
        tr_table.pop(0)
        for i in range(len(th_table)):
            table.append(f'{th_table[i].text}:{tr_table[i].text}\n')

        if th_table[0].text != 'Название, символ, номер':
            await message.answer('Проверьте правильность написания')
        else:
            await message.answer(''.join(table))
    except:
        AttributeError
        await message.answer('Проверьте правильность написания')

    

    
    
        





    
    

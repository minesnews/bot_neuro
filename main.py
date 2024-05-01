import aiogram
import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards import keyboard

#Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()

@dp.message(F.text.lower() == 'старт')
@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!\nДоступные команды: /start, /stop, /user, /info\nВы так же можете написать следующие сообщения: привет; как дела; какой сегодня день (в зависимости от рандома выбирает какой сегодня день) и бот ответит\nДоступные фильтры: рандом, старт, юзер, стоп, инфо', reply_markup=keyboard)

# @dp.message(Command(commands=['start']))
@dp.message(F.text.lower() == 'рандом')
async def info(message: types.Message):
    number = random.randint(0, 100)
    await message.answer(f'Привет, твоё число: {number}!')

@dp.message(F.text.lower() == 'стоп')
@dp.message(Command(commands=['stop']))
async def stop(message: types.Message):
    await message.answer(f'Пока, {message.from_user.full_name}!')
    #print(message)

@dp.message(F.text.lower() == 'юзер')
@dp.message(Command(commands=['user']))
async def user(message: types.Message):
    await message.answer(f'Информация о вас: имя: {message.from_user.first_name}, фамилия: {message.from_user.last_name}, имя пользователя: @{message.from_user.username}')

@dp.message(F.text.lower() == 'инфо')
@dp.message(Command(commands=['info']))
@dp.message(F.text.lower() == 'инфо')
async def info(message: types.Message):
    await message.answer(f'Информация о боте: имя: Ghost Automaton, имя пользователя: @Elijah_Animus_bot')


@dp.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')
    elif 'как дела' in message.text.lower():
        await message.reply('Нормально, а у тебя?')
    elif 'какой сегодня день' in message.text.lower():
        rand = random.randint(0, 2)
        day = ''
        if rand == 0:
            day = 'хороший'
        elif rand == 1:
            day = 'отличный'
        else:
            day = 'превосходный'
        await message.reply(f'Сегодня {day} день! (рандом= {rand})')
    else:
        await message.reply('Не понимаю тебя...')

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

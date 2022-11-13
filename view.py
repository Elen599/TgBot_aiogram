# Здесь все функции отправляющие сообщения
from aiogram import types
from bot import bot


async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           f'Это игра в конфетки\n\n'
                           f'Ознакомься с условиями игры с ботом:\nНа столе лежат 150 конфет.\nКаждый игрок делает ход друг после друга.\n'
                           f'За один ход игрок может взять от 1 до 10 конфет.\n'
                           f'Выигрывает тот, кто возьмет конфеты последним.\n'
                           f'Определи сколько конфет нужно взять первому игроку,\n чтобы забрать все конфеты у своего конкурента.\n'
                           f'Первый ход определяется жеребьёвкой.\n\n'
                           f'Для начала игры нажмите: /play\n'
                           f'Для остановки игры нажмите: /finish')


async def message(message, text):
    await bot.send_message(message.from_user.id, text)
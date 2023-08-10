from tgbot.loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram import types

@dp.message_handler()
async def no_sub(message: types.Message):
    await message.answer('Что-то пошло не так! Напишите команду /start')
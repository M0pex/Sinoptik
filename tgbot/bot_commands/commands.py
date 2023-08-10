from aiogram import Dispatcher
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault



commands = [
    BotCommand("start", "Перезапуск бота")
]



async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(commands, scope=BotCommandScopeDefault())





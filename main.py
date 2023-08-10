import os
import sys

import logging

import asyncio


from aiogram import executor, Dispatcher
from tgbot.handlers import dp
from tgbot.bot_commands.commands import set_commands
from tgbot.db.database import db
from tgbot.utils.session import RequestsSession
from tgbot.utils import setup_middlewares
from tgbot.handlers.user.alarm_handlers import send_message_scheduler, send_message_scheduler_evry



logging.basicConfig(level=logging.INFO)





async def on_startup(dp: Dispatcher):
    await dp.bot.delete_webhook()
    await dp.bot.get_updates(offset=-1)
    dp.bot['rSession'] = RequestsSession()
    await set_commands(dp)


async def on_shutdown(dp: Dispatcher):
    rSession: RequestsSession = dp.bot['rSession']
    await rSession.close()

    await dp.storage.close()
    await dp.storage.wait_closed()
    await (await dp.bot.get_session()).close()

    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

# Запускаем планировщик задач
async def scheduler():
    tasks = [
        asyncio.create_task(send_message_scheduler()),
        asyncio.create_task(send_message_scheduler_evry())
    ]
    await asyncio.gather(*tasks)


async def main():
    tasks = [
        asyncio.create_task(dp.start_polling()),
        asyncio.create_task(scheduler())
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    db()
    setup_middlewares(dp)
    asyncio.run(main())
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)


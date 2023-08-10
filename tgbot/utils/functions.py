from tgbot.db.db_logging import log_user
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

class ExistsUserMiddleware(BaseMiddleware):
    def __init__(self):
        self.prefix = "key_prefix"
        super(ExistsUserMiddleware, self).__init__()


    async def on_pre_process_message(self, message: types.Message, data: dict):
        user = message.from_user

        await self.add_log_user(user)

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        user = query.from_user

        await self.add_log_user(user)

    async def add_log_user(self, user):
        # Your logging logic here using the `user` object

        log_user(user)

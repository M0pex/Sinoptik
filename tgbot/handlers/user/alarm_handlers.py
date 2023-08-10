import asyncio



from tgbot.loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram import types
from tgbot.db.db_logging import update_user_info, get_users_with_alarm, get_userx, get_users_to_notify
from tgbot.buttons.inline_user import alarm_time, weather_day_choose
from tgbot.handlers.user.user_handlers import message_user
from tgbot.locales.uk.strings import _

from datetime import datetime, time

@dp.message_handler(text=['Утро, день', 'Ранок, день'], state="*")
async def twice_day(message: types.Message, state: FSMContext):
    await state.finish()
    get_user = get_userx(user_id=message.from_user.id)
    lang = get_user['lang']

    update_user_info(message.from_user.id, alarm=None)
    update_user_info(message.from_user.id, evry_day=1)
    await message.answer(_('Уведомления о погоде будут приходить ежедневно в 7:00 и в 15:00', lang))


@dp.message_handler(text='На завтра', state="*")
async def every_day(message: types.Message, state: FSMContext):
    await state.finish()
    get_user = get_userx(user_id=message.from_user.id)
    lang = get_user['lang']

    await message.answer(_('Укажите время, когда присылать погодные уведомления', lang), reply_markup=alarm_time())


@dp.callback_query_handler(text_startswith='time_for_alarm', state="*")
async def chosen_time(query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    get_user = get_userx(user_id=query.from_user.id)
    lang = get_user['lang']

    time = query.data.split("/")[1]

    update_user_info(query.from_user.id, alarm=time)
    update_user_info(query.from_user.id, evry_day=0)
    await query.message.delete()
    await query.message.answer(_(f'Уведомления будут приходить в ', lang) + time)




@dp.message_handler(text=['Отписаться', 'Відписатися'], state="*")
async def twice_day(message: types.Message, state: FSMContext):
    await state.finish()
    get_user = get_userx(user_id=message.from_user.id)
    lang = get_user['lang']

    update_user_info(message.from_user.id, alarm=None)
    update_user_info(message.from_user.id, evry_day=0)
    await message.answer(_('Бот больше не будет отправлять уведомления о погоде', lang))


async def send_message_to_user(user_id: int, message: str):


    get_user = get_userx(user_id=user_id)
    await bot.send_message(user_id, message, reply_markup=weather_day_choose(get_user['city'], user_id))


async def send_message_scheduler():
    while True:
        current_time = datetime.now().time()
        scheduled_time = current_time.replace(second=0, microsecond=0)

        # Получаем список пользователей с заполненным столбцом alarm
        users = get_users_with_alarm()

        for user_id, alarm in users:
            alarm_time = datetime.strptime(alarm, '%H:%M').time()

            if scheduled_time == alarm_time:

                await send_message_to_user(user_id, message_user(user_id))

        # Ожидаем 1 минуту перед проверкой следующего времени
        await asyncio.sleep(60)
        print('wait')


async def send_message_scheduler_evry():
    while True:
        current_time = datetime.now().time()
        scheduled_time = current_time.replace(second=0, microsecond=0)


            # Получаем список пользователей, которым нужно отправить сообщение
        users = get_users_to_notify()

        for user_id, alarm in users:
            # Проверяем, соответствует ли текущее время 7:00 или 15:00
            if scheduled_time == time(7, 0) or scheduled_time == time(15, 0):

                await send_message_to_user(user_id, message_user(user_id))

        # Ожидаем 1 минуту перед проверкой следующего времени
        await asyncio.sleep(60)
        print('waitsec')
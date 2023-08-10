from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime, timedelta
from tgbot.locales.uk.strings import _
from tgbot.db.db_logging import get_userx

data_time_today = datetime.now()
formated_data_time = data_time_today + timedelta(days=1)
data_time = formated_data_time.strftime('%Y-%m-%d')

def weather_day_choose(city, user_id):

    get_user = get_userx(user_id=user_id)
    lang = get_user['lang']

    keyboard = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton("Завтра", url=f"https://sinoptik.ua/погода-{city}/{data_time}")
    ).add(
        InlineKeyboardButton(_("7 дней", lang), url=f"https://sinoptik.ua/погода-{city}")
    ).add(
        InlineKeyboardButton(_("10 дней", lang), url=f"https://sinoptik.ua/погода-{city}/10-дней")
    )

    keyboard_ua = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton("Завтра", url=f"https://ua.sinoptik.ua/погода-{city}/{data_time}")
    ).add(
        InlineKeyboardButton(_("7 дней", lang), url=f"https://ua.sinoptik.ua/погода-{city}")
    ).add(
        InlineKeyboardButton(_("10 дней", lang), url=f"https://ua.sinoptik.ua/погода-{city}/10-днів")
    )

    if lang == 'uk':
        return keyboard_ua
    else:
        return keyboard

def alarm_time():

    keyboard = InlineKeyboardMarkup(row_width=3)

    buttons = [

        InlineKeyboardButton("06:00", callback_data="time_for_alarm/06:00"),

        InlineKeyboardButton("07:00", callback_data="time_for_alarm/07:00"),

        InlineKeyboardButton("08:00", callback_data="time_for_alarm/08:00"),

        InlineKeyboardButton("09:00", callback_data="time_for_alarm/09:00"),

        InlineKeyboardButton("10:00", callback_data="time_for_alarm/10:00"),

        InlineKeyboardButton("11:00", callback_data="time_for_alarm/11:00"),

        InlineKeyboardButton("12:00", callback_data="time_for_alarm/12:00"),

        InlineKeyboardButton("13:00", callback_data="time_for_alarm/13:00"),

        InlineKeyboardButton("14:00", callback_data="time_for_alarm/14:00"),

        InlineKeyboardButton("15:00", callback_data="time_for_alarm/15:00"),

        InlineKeyboardButton("16:00", callback_data="time_for_alarm/16:00"),

        InlineKeyboardButton("17:00", callback_data="time_for_alarm/17:00"),

        InlineKeyboardButton("18:00", callback_data="time_for_alarm/18:00"),

        InlineKeyboardButton("19:00", callback_data="time_for_alarm/19:00"),

        InlineKeyboardButton("20:00", callback_data="time_for_alarm/20:00"),

        InlineKeyboardButton("21:00", callback_data="time_for_alarm/21:00"),

        InlineKeyboardButton("22:00", callback_data="time_for_alarm/22:00"),

        InlineKeyboardButton("23:00", callback_data="time_for_alarm/23:00"),

    ]

    keyboard.add(*buttons)

    return keyboard


def choose_lang():

    keyboard = InlineKeyboardMarkup(row_width=2)

    buttons = [

        InlineKeyboardButton('🇺🇦', callback_data='choose_language:uk'),

        InlineKeyboardButton('🇷🇺', callback_data='choose_language:ru'),

    ]

    keyboard.add(*buttons)

    return keyboard

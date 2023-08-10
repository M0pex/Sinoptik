from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def sub_on_channel():
    keyboard = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton("Подписаться", url="https://t.me/+7qAId_MKqeAyOGIy")
    ).add(
        InlineKeyboardButton("Готово", callback_data="check_sub")
    )

    return keyboard
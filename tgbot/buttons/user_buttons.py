from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from tgbot.db.db_logging import get_userx
from tgbot.locales.uk.strings import _


def menu_buttons(user_id):
    get_user = get_userx(user_id=user_id)
    lang = get_user['lang']

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(_('⛅️Погода', lang), _('⚙️Настройки', lang))

    return keyboard

def setting_buttons(user_id):
    get_user = get_userx(user_id=user_id)
    lang = get_user['lang']


    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(_('📩Уведомления', lang))
    keyboard.row(_('🌐Язык', lang), _('🏙Город', lang))
    keyboard.row(_('⬅️Назад', lang))

    return keyboard


def alarm_buttons(user_id):
    get_user = get_userx(user_id=user_id)
    lang = get_user['lang']

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(_("Утро, день", lang), "На завтра")
    keyboard.row(_("Отписаться", lang))
    keyboard.row(_("Главная", lang))

    return keyboard
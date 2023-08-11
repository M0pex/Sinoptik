from tgbot.loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram import types
from tgbot.buttons.user_buttons import menu_buttons, setting_buttons, alarm_buttons
from tgbot.parser.parsing import get_html, get_data, get_html_ua, get_html_us
from tgbot.db.db_logging import update_user_info, get_userx
from tgbot.buttons.inline_user import weather_day_choose, choose_lang
from tgbot.locales.uk.strings import _

from datetime import datetime


@dp.message_handler(text='/start', state="*")
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    get_user = get_userx(user_id=message.from_user.id)
    lang = get_user['lang']

    await message.answer(_('Привет! Я погодный бот. Я буду отправлять тебе погоду в нужное для тебя время', lang))
    await message.answer(_('Введите название города', lang), reply_markup=menu_buttons(message.from_user.id))
    await state.set_state('wait_city')

@dp.message_handler(text=['🏙Город', '🏙Місто', '🏙City'], state="*")
async def choose_city(message: types.Message, state: FSMContext):
    get_user = get_userx(user_id=message.from_user.id)
    lang = get_user['lang']

    await message.answer(_('Введите название города', lang), reply_markup=menu_buttons(message.from_user.id))
    await state.set_state('wait_city')



@dp.message_handler(content_types='text', state="wait_city")
async def show_city(message: types.Message, state: FSMContext):

    get_user = get_userx(user_id=message.from_user.id)
    lang = get_user['lang']


    try:
        if lang == 'ru':
            html = get_html(get_user['city'])
            data = get_data(html)
        elif lang == 'uk':
            html = get_html_ua(get_user['city'])
            data = get_data(html)
        else:
            html = get_html_us(get_user['city'])
            data = get_data(html)


        if data[7] == '-':
            rain = _('Отсутствует', lang)
        else:
            rain = data[7] + '%'

        msg_for_user = '🏙<strong>' + data[0] + '</strong>\n' + datetime.now().strftime('%d-%m-%Y') + _(
            '\n\n<b>Текущая</b>', lang) + '' \
                                          '\n🌡' + data[1] + _('C (Ощущается как ', lang) + data[
                           2] + 'C)\n' \
                                '<u>' + data[3] + _('</u>\n\n🌀Давление: <u>', lang) + data[4] + ' мм рт.ст.</u>\n' \
                                                                                                '' + _(
            '💧Влажность: <u>', lang) + data[5] + '%</u>\n' \
                                                 '' + _('💨Ветер: <u>', lang) + data[6] + _(
            '</u>\n☔️Вероятность осадков: <u>', lang) + rain + _('</u>\n\n\n<b>Дневная</b>\n', lang) + '' \
                                                                                                       '<u>' + data[
                           8] + '</u> ' + data[16] + 'C' + '\n' \
                                                           '<u>' + data[9] + '</u> ' + data[17] + 'C' + '\n' \
                                                                                                        '<u>' + data[
                           10] + '</u> ' + data[18] + 'C' + '\n' \
                                                            '<u>' + data[11] + '</u> ' + data[19] + 'C' + '\n\n' \
                                                                                                          '<u>' + data[
                           12] + '</u> ' + data[20] + 'C' + '\n' \
                                                            '<u>' + data[13] + '</u> ' + data[21] + 'C' + '\n' \
                                                                                                          '<u>' + data[
                           14] + '</u> ' + data[22] + 'C' + '\n' \
                                                            '<u>' + data[15] + '</u> ' + data[23] + 'C' + '\n'


        await message.answer(msg_for_user, reply_markup=weather_day_choose(message.text, message.from_user.id))
        update_user_info(message.from_user.id, city=message.text)
        update_user_info(message.from_user.id, evry_day=1)
        await state.finish()


    except AttributeError as e:
        await message.answer(_('Похоже вы указали город не правильно.\nПопробуйте ввести еще раз', lang))

@dp.message_handler(text=['⛅️Погода', '⛅️Weather'], state="*")
async def show_weather(message: types.Message, state: FSMContext):



    get_user = get_userx(user_id=message.from_user.id)
    lang = get_user['lang']

    try:

        if lang == 'ru':
            html = get_html(get_user['city'])
            data = get_data(html)
        elif lang == 'uk':
            html = get_html_ua(get_user['city'])
            data = get_data(html)
        else:
            html = get_html_us(get_user['city'])
            data = get_data(html)
        if data[7] == '-':
            rain = _('Отсутствует', lang)
        else:
            rain = data[7] + '%'


        msg_for_user = '🏙<strong>' + data[0] + '</strong>\n' + datetime.now().strftime('%d-%m-%Y') + _('\n\n<b>Текущая</b>', lang) + '' \
                               '\n🌡' + data[1] + _('C (Ощущается как ', lang) + data[
                               2] + 'C)\n' \
                               '<u>' + data[3] + _('</u>\n\n🌀Давление: <u>', lang) + data[4] + ' мм рт.ст.</u>\n' \
                               '' + _('💧Влажность: <u>', lang) + data[5] + '%</u>\n' \
                               '' + _('💨Ветер: <u>', lang) + data[6] + _('</u>\n☔️Вероятность осадков: <u>', lang) + rain + _('</u>\n\n\n<b>Дневная</b>\n', lang) + '' \
                                '<u>' + data[8] + '</u> ' + data[16] + 'C'   + '\n' \
                                '<u>' + data[9] + '</u> ' + data[17] + 'C'   + '\n' \
                                '<u>' + data[10] + '</u> ' + data[18] + 'C'   + '\n' \
                                '<u>' + data[11] + '</u> ' + data[19] + 'C'   + '\n\n' \
                                '<u>' + data[12] + '</u> ' + data[20] + 'C'   + '\n' \
                                '<u>' + data[13] + '</u> ' + data[21] + 'C'   + '\n' \
                                '<u>' + data[14] + '</u> ' + data[22] + 'C'   + '\n' \
                                '<u>' + data[15] + '</u> ' + data[23] + 'C'   + '\n'

        await message.answer(msg_for_user, reply_markup=weather_day_choose(get_user['city'], message.from_user.id))
        await state.finish()

    except AttributeError as e:
        await message.answer(_('Похоже вы указали город не правильно.\nПопробуйте ввести еще раз', lang))


def message_user(user_id):


    get_user = get_userx(user_id=user_id)
    lang = get_user['lang']


    try:
        msg_for_user = ''

        if lang == 'ru':
            html = get_html(get_user['city'])
            data = get_data(html)
        elif lang == 'uk':
            html = get_html_ua(get_user['city'])
            data = get_data(html)
        else:
            html = get_html_us(get_user['city'])
            data = get_data(html)

        if data[7] == '-':
            rain = _('Отсутствует', lang)
        else:
            rain = data[7] + '%'

        msg_for_user = '🏙<strong>' + data[0] + '</strong>\n' + datetime.now().strftime('%d-%m-%Y') + _(
            '\n\n<b>Текущая</b>', lang) + '' \
                                          '\n🌡' + data[1] + _('C (Ощущается как ', lang) + data[
                           2] + 'C)\n' \
                                '<u>' + data[3] + _('</u>\n\n🌀Давление: <u>', lang) + data[4] + ' мм рт.ст.</u>\n' \
                                                                                                '' + _(
            '💧Влажность: <u>', lang) + data[5] + '%</u>\n' \
                                                 '' + _('💨Ветер: <u>', lang) + data[6] + _(
            '</u>\n☔️Вероятность осадков: <u>', lang) + rain + _('</u>\n\n\n<b>Дневная</b>\n', lang) + '' \
                                                                                                       '<u>' + data[
                           8] + '</u> ' + data[16] + 'C' + '\n' \
                                                           '<u>' + data[9] + '</u> ' + data[17] + 'C' + '\n' \
                                                                                                        '<u>' + data[
                           10] + '</u> ' + data[18] + 'C' + '\n' \
                                                            '<u>' + data[11] + '</u> ' + data[19] + 'C' + '\n\n' \
                                                                                                          '<u>' + data[
                           12] + '</u> ' + data[20] + 'C' + '\n' \
                                                            '<u>' + data[13] + '</u> ' + data[21] + 'C' + '\n' \
                                                                                                          '<u>' + data[
                           14] + '</u> ' + data[22] + 'C' + '\n' \
                                                            '<u>' + data[15] + '</u> ' + data[23] + 'C' + '\n'

        return msg_for_user

    except AttributeError as e:
        pass




@dp.message_handler(text=['⚙️Настройки', '⚙️Налаштування', '⚙️Settings'], state="*")
async def settings(message: types.Message, state: FSMContext):
    await state.finish()
    get_user = get_userx(user_id=message.from_user.id)
    lang = get_user['lang']

    await message.answer(_('<b>Настройки</b>', lang), reply_markup=setting_buttons(message.from_user.id))



@dp.message_handler(text=['📩Уведомления', '📩Повідомлення', '📩Message'], state="*")
async def alarms(message: types.Message, state: FSMContext):
    await state.finish()
    get_user = get_userx(user_id=message.from_user.id)
    lang = get_user['lang']


    await message.answer(_('Укажите в какой период нужно отправлять уведомления о погоде', lang), reply_markup=alarm_buttons(message.from_user.id))



@dp.message_handler(text=['⬅️Назад', 'Главная', 'Головна', '⬅️Back', 'Menu'], state="*")
async def back(message: types.Message, state: FSMContext):
    await state.finish()
    get_user = get_userx(user_id=message.from_user.id)
    lang = get_user['lang']

    await message.answer(_('<b>Главное меню</b>', lang), reply_markup=menu_buttons(message.from_user.id))

@dp.message_handler(text=['🌐Язык', '🌐Мова', '🌐Language'], state="*")
async def change_lang(message: types.Message, state: FSMContext):
    await state.finish()

    get_user = get_userx(user_id=message.from_user.id)
    lang = get_user['lang']

    if lang == 'ru':
        ico = _('Русский🇷🇺', lang)
    elif lang == 'uk':
        ico = _('Украинский🇺🇦', lang)
    else:
        ico = _('Английский🇬🇧', lang)

    await message.answer(_('Текущий язык: ', lang) + ico + _('\nВыберите язык: ', lang), reply_markup=choose_lang())


@dp.callback_query_handler(text_startswith='choose_language', state="*")
async def language_choosen(query: types.CallbackQuery, state: FSMContext):
    await state.finish()

    lang = query.data.split(":")[1]

    update_user_info(query.from_user.id, lang=lang)

    if lang == 'ru':
        mova = '🇷🇺'
    elif lang == 'uk':
        mova = '🇺🇦'
    else:
        mova = '🇬🇧'

    await query.message.delete()
    await query.message.answer(_('Ваш язык успешно изменен на ', lang) + mova, reply_markup=menu_buttons(query.from_user.id))







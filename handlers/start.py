from loader import bot, dp
from aiogram import types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ParseMode, ReplyKeyboardMarkup, KeyboardButton

from handlers.dir.DBCommands import DBCommands
import handlers.dir.states as states
from config import ADMINS
import handlers.dir.keyboards as kb
import handlers.dir.google_sheets as sheets

db = DBCommands()



@dp.message_handler(commands=['start'])
async def start(message: Message):
    db.create()
    i=0
    videos_man = db.select_all_videos_man().fetchall()
    videos_woman = db.select_all_videos_woman().fetchall()
    if len(videos_man)<9:
        while i<9:
            db.add_video_man(id=i+1)
            i+=1

    if len(videos_woman)<9:
        while i<9:
            db.add_video_woman(id=i+1)
            i+=1
    video_link = kb.inline_url('Ссылка на видео', 'https://youtube.com/')
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         'Это чат-бот проекта с совершенно особенными тренировками "Крутое тело".\n'
                         'Ниже мы приготовили для тебя ознакомительное видео'
                         ' - смотри внимательно:',
                         reply_markup=video_link)

    await message.answer('Каждый понедельник мы принимаем новеньких!'
                         ' Чтобы присоединиться к тренировкам по программе проекта,'
                         ' нужно зарегистрироваться на сайте www.krutoetelo.ru')

    await message.answer('Чтобы дальше наше общение было более персональным, '
                         'укажи пожалуйста свой пол '
                         '(просто нажми на соответствующую кнопку ниже):', reply_markup=kb.mg_keyboard)





@dp.callback_query_handler(lambda c: c.data == 'man' or c.data=='woman')
async def man_woman(query: CallbackQuery):

    chatid = query.from_user.id
    username = query.from_user.username
    name = query.from_user.full_name
    gender = query.data
    users = db.select_all_users().fetchall()
    i=0
    for user in users:
        if chatid==user[0]:
            i+=1
    if i==0:
        if username == None:
            await bot.send_message(chat_id=chatid, text='У вас отсутсвует никнейм в телеграме')
            return
        db.add_user(par=(chatid, username, name, gender))


    if gender == 'man':
        await bot.send_message(chat_id=chatid, text='Если ты уже зарегистрировался,'
                                                    ' просто дождись ближайшего'
                                                    ' понедельника. И прямо здесь'
                                                    ' начнутся твои тренировки с'
                                                    ' персональной нагрузкой по системе'
                                                    ' Smart Muscle System.')
    elif gender == 'woman':
        await bot.send_message(chat_id=chatid, text='Если ты уже зарегистрировалась,'
                                                    ' просто дождись ближайшего'
                                                    ' понедельника. И прямо здесь'
                                                    ' начнутся твои тренировки с'
                                                    ' персональной нагрузкой по системе'
                                                    ' Smart Muscle System.')
    site = kb.inline_url('Зарегистрироваться', 'www.krutoetelo.ru')
    await bot.send_message(chat_id=chatid, text='Если у тебя ещё нет регистрации,'
                                                ' скорее жми на кнопку'
                                                ' "Зарегистрироваться" ниже:',
                           reply_markup=site)
    await bot.send_message(chat_id=chatid, text='Мы ждём тебя, чтобы стать круче вместе!')









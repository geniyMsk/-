from loader import bot, dp
from aiogram import types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ParseMode, ReplyKeyboardMarkup, KeyboardButton

from handlers.dir.DBCommands import DBCommands
import handlers.dir.states as states
from config import ADMINS
import handlers.dir.keyboards as kb
import handlers.dir.google_sheets as sheets
import handlers.dir.update_def as update
db = DBCommands()


#async def update_schedule():
#    for admin in ADMINS:
#        try:
#            await update.input(bot=bot, chat_id=admin)
#            await update.output(bot=bot, chat_id=admin)
#            await update.messages(bot=bot, chat_id=admin)
#        except Exception as error:
#            bot.send_message(chat_id=546476479, text='Произошла ошибка:' + f'{error}')


for admin in ADMINS:
    @dp.message_handler(user_id = admin, commands=['update'], state='*')
    async def update_all(message: Message):
        message_id = message.message_id
        chatid = message.from_user.id
        await message.answer('...')
        await message.answer('...')
        await message.answer('...')
        await message.answer('...')
        await message.answer('...')
        await message.answer('Обновление данных...')

        await update.input(bot=bot, chat_id=chatid, message_id=message_id)
        await update.delete_output(bot=bot, chat_id=chatid, message_id=message_id)
        await update.messages(bot=bot, chat_id=chatid, message_id=message_id)
        await bot.edit_message_text(message_id=message_id+6, chat_id=chatid, text='Обновление завершено')






    @dp.message_handler(user_id=admin, commands=['all'])
    async def all(message: Message):
        users = db.select_all_users().fetchall()
        name = message.get_args()
        text = ''
        for user in users:
            if len(text)<4096:
                text += f'{users.index(user)+1}. {user[2]} - {user[1]}\n'
            else:
                text = 'Слишком много пользователей'
        await message.answer(text)


    @dp.message_handler(user_id=admin, content_types=['video'])
    async def add_video_command(message: Message):
        caption = message.caption
        file_id = message.video.file_id
        if caption[:6] != '/video':
            return
        args = caption[7:]
        a = args.split(' ')
        gender = a[0]
        try:
            id = int(a[1])
        except:
            return

        if gender=='man':
            db.update_video_man(par=(file_id, id))
            await message.answer(f'Видео {id} для мужчин загружено')
        elif gender=='woman':
            db.update_video_woman(par=(file_id, id))
            await message.answer(f'Видео {id} для женщин загружено')
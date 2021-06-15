from loader import bot, dp, scheduler
from aiogram import types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ParseMode, ReplyKeyboardMarkup, KeyboardButton

from handlers.dir.DBCommands import DBCommands
import handlers.dir.states as states
from config import ADMINS
import handlers.dir.keyboards as kb
import handlers.dir.google_sheets as sheets
import handlers.dir.update_def as update

db = DBCommands()






for admin in ADMINS:
    @dp.message_handler(commands=['mail'], user_id = admin, state='*')
    async def mailing1(message: Message):
        usernames = db.select_username_input().fetchall()
        chatids = []

        for username in usernames:
            user = db.select_users(par=(username[0],)).fetchone()
            if user != None:
                chatids.append([user[0], user[3]])

        chatids_man = []
        chatids_woman = []
        for chatid in chatids:

            if chatid[1] == 'man':
                chatids_man.append(chatid[0])
            elif chatid[1] == 'woman':
                chatids_woman.append(chatid[0])
        for chatid_man in chatids_man:
            name = (await bot.get_chat(chat_id=chatid_man)).full_name
            text = f'Привет, {name}\n' + db.select_message_man(id=(1,)).fetchone()[0]
            try:
                await bot.send_message(chat_id=chatid_man, text=text, reply_markup=kb.start_training)
            except:
                pass
        for chatid_woman in chatids_woman:
            name = (await bot.get_chat(chat_id=chatid_woman)).full_name
            text = f'Привет, {name}\n' + db.select_message_woman(id=(1,)).fetchone()[0]
            try:
                await bot.send_message(chat_id=chatid_woman, text=text, reply_markup=kb.start_training)
            except:
                pass

async def mailing():
    usernames = db.select_username_input().fetchall()
    chatids = []

    for username in usernames:
        user = db.select_users(par=(username[0],)).fetchone()
        if user != None:
            chatids.append([user[0], user[3]])

    chatids_man = []
    chatids_woman = []
    for chatid in chatids:

        if chatid[1] == 'man':
            chatids_man.append(chatid[0])
        elif chatid[1] == 'woman':
            chatids_woman.append(chatid[0])

    for chatid_man in chatids_man:

        name = (await bot.get_chat(chat_id=chatid_man)).full_name
        text = f'Привет, {name}\n' + db.select_message_man(id=(1,)).fetchone()[0]
        try:
            await bot.send_message(chat_id=chatid_man, text=text, reply_markup=kb.start_training)
        except:
            pass
    for chatid_woman in chatids_woman:
        name = (await bot.get_chat(chat_id=chatid_woman)).full_name
        text = f'Привет, {name}\n' + db.select_message_woman(id=(1,)).fetchone()[0]
        try:
            await bot.send_message(chat_id=chatid_woman, text=text, reply_markup=kb.start_training)
        except:
            pass

@dp.callback_query_handler(lambda c:c.data=="start_training", state=[None, states.TRAIN.step0])
async def start_training(query: CallbackQuery):
    chatid = query.from_user.id
    gender = db.select_gender(chatid=(chatid,)).fetchone()[0]
    input = db.select_input(chatid=(chatid,)).fetchone()



    if gender=='man':
        text = db.select_message_man(id=(2,)).fetchone()[0]
        url = db.select_message_man(id=(3,)).fetchone()[0]
        link = kb.inline_url('Видео', url)
        await bot.send_message(chat_id=chatid, text=text, reply_markup=link)
        text = db.select_message_man(id=(4,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        video = db.select_video_man(id=(1,)).fetchone()[0]
        await bot.send_video(chat_id=chatid,video=video)
        await bot.send_message(chat_id=chatid, text=f'"{input[3]}" раз', reply_markup=kb.done_man)
        await states.TRAIN.step1.set()


    elif gender == 'woman':
        text = db.select_message_woman(id=(2,)).fetchone()[0]
        url = db.select_message_woman(id=(3,)).fetchone()[0]
        link = kb.inline_url('Видео', url)
        await bot.send_message(chat_id=chatid, text=text, reply_markup=link)
        text = db.select_message_woman(id=(4,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        video = db.select_video_woman(id=(1,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)
        await bot.send_message(chat_id=chatid, text=f'"{input[3]}" раз', reply_markup=kb.done_woman)
        await states.TRAIN.step1.set()

@dp.callback_query_handler(lambda c:c.data=="done", state=states.TRAIN.step1)
async def start_training(query: CallbackQuery):
    chatid = query.from_user.id
    gender = db.select_gender(chatid=(chatid,)).fetchone()[0]
    input = db.select_input(chatid=(chatid,)).fetchone()

    if gender=='man':
        text = db.select_message_man(id=(5,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        video = db.select_video_man(id=(2,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)
        await bot.send_message(chat_id=chatid, text=f'"{input[6]}" раз', reply_markup=kb.done_man)
        await states.TRAIN.step2.set()


    elif gender == 'woman':
        text = db.select_message_woman(id=(5,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        video = db.select_video_woman(id=(2,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)
        await bot.send_message(chat_id=chatid, text=f'"{input[6]}" раз', reply_markup=kb.done_woman)
        await states.TRAIN.step2.set()


@dp.callback_query_handler(lambda c:c.data=="done", state=states.TRAIN.step2)
async def start_training(query: CallbackQuery):
    chatid = query.from_user.id
    gender = db.select_gender(chatid=(chatid,)).fetchone()[0]
    input = db.select_input(chatid=(chatid,)).fetchone()
    if gender == 'man':
        text = db.select_message_man(id=(6,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        video = db.select_video_man(id=(3,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)
        await bot.send_message(chat_id=chatid, text=f'"{input[7]}" раз', reply_markup=kb.done_man)
        await states.TRAIN.step3.set()


    elif gender == 'woman':
        text = db.select_message_woman(id=(6,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        video = db.select_video_woman(id=(3,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)
        await bot.send_message(chat_id=chatid, text=f'"{input[7]}" раз', reply_markup=kb.done_woman)
        await states.TRAIN.step3.set()

@dp.callback_query_handler(lambda c:c.data=="done", state=states.TRAIN.step3)
async def start_training(query: CallbackQuery):
    chatid = query.from_user.id
    gender = db.select_gender(chatid=(chatid,)).fetchone()[0]
    input = db.select_input(chatid=(chatid,)).fetchone()
    if gender == 'man':
        text = db.select_message_man(id=(7,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        text = db.select_message_man(id=(8,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        video = db.select_video_man(id=(4,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)
        await bot.send_message(chat_id=chatid, text=f'*Немного больше* "{input[4]}" раз',
                               parse_mode=ParseMode.MARKDOWN)
        text = db.select_message_man(id=(9,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        await states.TRAIN.step4.set()


    elif gender == 'woman':
        text = db.select_message_woman(id=(7,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        text = db.select_message_woman(id=(8,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        video = db.select_video_woman(id=(4,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)
        await bot.send_message(chat_id=chatid, text=f'*Немного больше* "{input[4]}" раз',
                               parse_mode=ParseMode.MARKDOWN)
        text = db.select_message_woman(id=(9,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        await states.TRAIN.step4.set()

@dp.message_handler(state=states.TRAIN.step4)
async def step4(message: Message):
    chatid = message.from_user.id
    username = message.from_user.username
    name = message.from_user.full_name
    try:
        output = int(message.text)
    except:
        await message.answer('Пожалуйста введите число')
        return
    i=0
    outputs = db.select_username_output().fetchall()
    for x in outputs:
        if x[0] == username:
            i+=1
    if i==0:
        db.add_output(par = (name, username, output))
    else:
        db.update_output(par=(output, username))

    gender = db.select_gender(chatid=(chatid,)).fetchone()[0]
    input = db.select_input(chatid=(chatid,)).fetchone()

    if gender == 'man':
        text = db.select_message_man(id=(10,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        video = db.select_video_man(id=(5,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)
        await bot.send_message(chat_id=chatid, text=f'"{input[6]}" раз', reply_markup=kb.done_man)
        await states.TRAIN.step5.set()
    elif gender=='woman':
        text = db.select_message_woman(id=(10,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        video = db.select_video_woman(id=(5,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)
        await bot.send_message(chat_id=chatid, text=f'"{input[6]}" раз', reply_markup=kb.done_woman)
        await states.TRAIN.step5.set()



@dp.callback_query_handler(lambda c:c.data=="done", state=states.TRAIN.step5)
async def start_training(query: CallbackQuery):
    chatid = query.from_user.id
    gender = db.select_gender(chatid=(chatid,)).fetchone()[0]
    input = db.select_input(chatid=(chatid,)).fetchone()
    if gender == 'man':
        text = db.select_message_man(id=(11,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        video = db.select_video_man(id=(6,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)
        await bot.send_message(chat_id=chatid, text=f'"{input[7]}" раз', reply_markup=kb.done_man)
        await states.TRAIN.step6.set()

    elif gender == 'woman':
        text = db.select_message_woman(id=(11,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        video = db.select_video_woman(id=(6,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)
        await bot.send_message(chat_id=chatid, text=f'"{input[7]}" раз', reply_markup=kb.done_woman)
        await states.TRAIN.step6.set()

@dp.callback_query_handler(lambda c:c.data=="done", state=states.TRAIN.step6)
async def start_training(query: CallbackQuery):
    chatid = query.from_user.id
    gender = db.select_gender(chatid=(chatid,)).fetchone()[0]
    input = db.select_input(chatid=(chatid,)).fetchone()
    name = query.from_user.full_name
    if gender == 'man':
        text = f'{name}' + db.select_message_man(id=(12,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        text = db.select_message_man(id=(13,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)

        video = db.select_video_man(id=(7,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)

        await bot.send_message(chat_id=chatid, text=f'*Больше* "{input[5]}" раз',
                               parse_mode=ParseMode.MARKDOWN)

        text = db.select_message_man(id=(14,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)

        await states.TRAIN.step7.set()

    elif gender == 'woman':
        text = f'{name}' + db.select_message_woman(id=(12,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        text = db.select_message_woman(id=(13,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)

        video = db.select_video_woman(id=(7,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)

        await bot.send_message(chat_id=chatid, text=f'*Больше* "{input[5]}" раз',
                               parse_mode=ParseMode.MARKDOWN)

        text = db.select_message_woman(id=(14,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)

        await states.TRAIN.step7.set()

@dp.message_handler(state=states.TRAIN.step7)
async def step7(message: Message):
    chatid = message.from_user.id
    username = message.from_user.username
    name = message.from_user.full_name
    try:
        output = int(message.text)
    except:
        await message.answer('Пожалуйста введите число')
        return
    db.update_output(par = (output, username))

    gender = db.select_gender(chatid=(chatid,)).fetchone()[0]
    input = db.select_input(chatid=(chatid,)).fetchone()

    if gender=='man':
        text =db.select_message_man(id=(15,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)

        video = db.select_video_man(id=(8,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)
        await bot.send_message(chat_id=chatid, text=f'"{input[6]}" раз', reply_markup=kb.done_man)

        await states.TRAIN.step8.set()


    elif gender=='woman':
        text = f'{name}' + db.select_message_woman(id=(15,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)

        video = db.select_video_woman(id=(8,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)

        await bot.send_message(chat_id=chatid, text=f'"{input[6]}" раз', reply_markup=kb.done_woman)

        await states.TRAIN.step8.set()

@dp.callback_query_handler(lambda c:c.data=="done", state=states.TRAIN.step8)
async def start_training(query: CallbackQuery):
    chatid = query.from_user.id
    gender = db.select_gender(chatid=(chatid,)).fetchone()[0]
    input = db.select_input(chatid=(chatid,)).fetchone()


    if gender == 'man':
        text = db.select_message_man(id=(16,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        video = db.select_video_man(id=(9,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)
        await bot.send_message(chat_id=chatid, text=f'"{input[7]}" раз', reply_markup=kb.done_man)
        await states.TRAIN.step9.set()

    elif gender == 'woman':
        text = db.select_message_woman(id=(16,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        video = db.select_video_woman(id=(9,)).fetchone()[0]
        await bot.send_video(chat_id=chatid, video=video)
        await bot.send_message(chat_id=chatid, text=f'"{input[7]}" раз', reply_markup=kb.done_woman)
        await states.TRAIN.step9.set()

@dp.callback_query_handler(lambda c:c.data=="done", state=states.TRAIN.step9)
async def start_training(query: CallbackQuery):
    chatid = query.from_user.id
    gender = db.select_gender(chatid=(chatid,)).fetchone()[0]
    if gender == 'man':
        text = db.select_message_man(id=(17,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        await states.TRAIN.step0.set()
    elif gender == 'woman':
        text = db.select_message_woman(id=(17,)).fetchone()[0]
        await bot.send_message(chat_id=chatid, text=text)
        await states.TRAIN.step0.set()
    await update.output(bot=bot)
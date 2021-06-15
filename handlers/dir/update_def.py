import handlers.dir.google_sheets as sheets
from handlers.dir.DBCommands import DBCommands
db = DBCommands()

async def input(bot, chat_id, message_id):
    try:
        db.delete_input()
        await bot.edit_message_text(message_id=message_id+1, chat_id=chat_id, text='Устаревшие данные input удалены из бд')
    except Exception as error:
        print(error)

    try:
        inputs = sheets.input()
        for input in inputs:
            db.insert_input(par=(input[0], input[1], input[2], input[3], input[4], input[5], input[6]))

            usernames_input = db.select_username_input().fetchall()
            users = db.select_all_users().fetchall()
            for user in users:
                for username in usernames_input:
                    if user[1]==username[0]:
                        chatid = user[0]
                        db.update_id_input(par=(chatid, user[1]))


        await bot.edit_message_text(message_id=message_id+2, chat_id=chat_id, text='Данные input успешно загружены в бд')
    except Exception as error:
        print(error)

async def output(bot):
    try:
        outputs = db.select_output().fetchall()
        sheets.clean_sheet('Output!A2:D')
        for output in outputs:
            n = outputs.index(output)
            sheets.output(n + 2, output[0], output[1], output[2], output[3])
        n = len(outputs)
        #await bot.send_message( chat_id=chat_id, text='Данные output загружены в таблицу')
    except Exception as error:
        await bot.send_message(chat_id=546476479, text='Произошла ошибка: ' + f'{error}')

async def delete_output(bot, chat_id, message_id):
    try:
        db.delete_output()
        await bot.edit_message_text(message_id=message_id + 3, chat_id=chat_id, text='Устаревшие данные output удалены из бд')
    except Exception as error:
        print(error)

async def messages(bot, chat_id, message_id):
    messages_man = sheets.messages_man()
    messages_woman = sheets.messages_woman()
    try:
        db.delete_messages()
        await bot.edit_message_text(message_id=message_id+4, chat_id=chat_id, text="Устаревший список сообщений удален из бд")
    except Exception as error:
        print(error)
    try:
        i=1
        for message1 in messages_man:
            db.add_messages_man(message=(i ,message1[0]))
            i += 1
        i=0
        for message1 in messages_woman:
            db.add_messages_woman(message=(i, message1[0],))
            i += 1
        await bot.edit_message_text(message_id=message_id+5, chat_id=chat_id, text="Сообщения загружены в бд")
    except Exception as error:
        print(error)

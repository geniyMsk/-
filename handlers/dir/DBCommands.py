import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    connection = psycopg2.connect(user="postgres",
                                  password="1111",
                                  host="127.0.0.1",
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute("""CREATE DATABASE cool_body_bot""")
    print('База данных "cool_body_bot" создана')
    cursor.close()
    connection.close()
except:
    pass
connection = psycopg2.connect(user="postgres",
                              password="1111",
                              host="127.0.0.1",
                              port="5432",
                              database = 'cool_body_bot')
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()
class DBCommands:

    def create(self):
        CREATE_USERS = f"""CREATE TABLE IF NOT EXISTS users 
            (id INTEGER UNIQUE, username TEXT, name TEXT, gender TEXT)"""
        CREATE_INPUT = f"""CREATE TABLE IF NOT EXISTS Input 
            (id INTEGER UNIQUE, name TEXT, username TEXT, cell1 INTEGER, cell2 INTEGER, cell3 INTEGER, 
            cell4 INTEGER, cell5 INTEGER)"""
        CREATE_OUTPUT = f"""CREATE TABLE IF NOT EXISTS Output 
                (name TEXT, username TEXT, cell1 INTEGER, cell2 INTEGER)"""
        CREATE_MESSAGES_MAN = f"""CREATE TABLE IF NOT EXISTS messages_man 
                    (ID INTEGER UNIQUE, message TEXT)"""
        CREATE_MESSAGES_WOMAN = f"""CREATE TABLE IF NOT EXISTS messages_woman 
                        (ID INTEGER UNIQUE, message TEXT)"""
        CREATE_VIDEOS_MAN = f"""CREATE TABLE IF NOT EXISTS videos_man 
                        (ID INTEGER UNIQUE, file_id TEXT)"""
        CREATE_VIDEOS_WOMAN = f"""CREATE TABLE IF NOT EXISTS videos_woman 
                                (ID INTEGER UNIQUE, file_id TEXT)"""

        cursor.execute(CREATE_USERS)
        cursor.execute(CREATE_INPUT)
        cursor.execute(CREATE_OUTPUT)
        cursor.execute(CREATE_MESSAGES_MAN)
        cursor.execute(CREATE_MESSAGES_WOMAN)
        cursor.execute(CREATE_VIDEOS_MAN)
        cursor.execute(CREATE_VIDEOS_WOMAN)



    def add_user(self, par):
        ADD_USER = f"""INSERT INTO users (id, username, name, gender) VALUES ({par[0]},'{par[1]}','{par[2]}','{par[3]}')"""
        command = ADD_USER
        cursor.execute(command, par)


    def update_users_gender(self, gender):
        UPDATE_USERS_GENDER = f"""UPDATE users SET gender = '{gender[0]}'"""
        command = UPDATE_USERS_GENDER
        cursor.execute(command, gender)


    def delete_input(self):
        DELETE_INPUT = f"""DELETE FROM input"""
        command = DELETE_INPUT
        cursor.execute(command)


    def insert_input(self, par):
        INSERT_INPUT = f"""INSERT INTO input (name, username, cell1, cell2, cell3, cell4, cell5)
                          VALUES 
                          ('{par[0]}', '{par[1]}', {par[2]}, {par[3]}, {par[4]}, {par[5]}, {par[6]})"""
        command = INSERT_INPUT
        cursor.execute(command, par)


    def select_all_users(self):
        SELECT_ALL_USERS = f"""SELECT * FROM users"""

        command = SELECT_ALL_USERS
        cursor.execute(command)
        return cursor


    def delete_output(self):
        DELETE_OUTPUT = f"""DELETE FROM output"""
        command = DELETE_OUTPUT
        cursor.execute(command)


    def add_output(self, par):
        ADD_OUTPUT = f"""INSERT INTO output (name, username, cell1) VALUES ('{par[0]}', '{par[1]}', {par[2]})"""
        command = ADD_OUTPUT
        cursor.execute(command, par)


    def update_output(self, par):
        UPDATE_OUTPUT = f"""UPDATE output SET cell2 = {par[0]} WHERE username = '{par[1]}'"""
        command = UPDATE_OUTPUT
        cursor.execute(command, par)
        return cursor


    def update_output_cell1(self, par):
        UPDATE_OUTPUT_CELL1 = f"""UPDATE output SET cell1 = {par[0]} WHERE username = '{par[1]}'"""
        command = UPDATE_OUTPUT_CELL1
        cursor.execute(command, par)
        return cursor



    def select_output(self):
        SELECT_OUTPUT = f"""SELECT * FROM output """

        command = SELECT_OUTPUT
        cursor.execute(command)
        return cursor


    def select_username_output(self):
        SELECT_USERNAME_OUTPUT = f"""SELECT username FROM output"""
        command = SELECT_USERNAME_OUTPUT
        cursor.execute(command)
        return cursor




    def select_username_input(self):
        SELECT_USERNAME_INPUT = f"""SELECT username FROM input"""
        command = SELECT_USERNAME_INPUT
        cursor.execute(command)
        return cursor



    def select_users(self, par):
        SELECT_USERS = f"""SELECT * FROM users WHERE username = '{par[0]}'"""
        command = SELECT_USERS
        cursor.execute(command, par)
        return cursor


    def select_gender(self, chatid):
        SELECT_GENDER = f"""SELECT gender FROM users WHERE id = {chatid[0]}"""
        command = SELECT_GENDER
        cursor.execute(command, chatid)
        return cursor


    def add_video_man(self,id):
        ADD_VIDEO_MAN = f"""INSERT INTO videos_man (id, file_id) VALUES ({id}, NULL)"""
        command = ADD_VIDEO_MAN
        cursor.execute(command)

    def add_video_woman(self,id):
        ADD_VIDEO_WOMAN = f"""INSERT INTO videos_woman (id, file_id) VALUES ({id}, NULL)"""
        command = ADD_VIDEO_WOMAN
        cursor.execute(command)



    def select_video_man(self, id):
        SELECT_VIDEO_MAN = f"""SELECT file_id FROM videos_man WHERE id = {id[0]}"""
        command = SELECT_VIDEO_MAN
        cursor.execute(command, id)
        return cursor

    def select_video_woman(self, id):
        SELECT_VIDEO_WOMAN = f"""SELECT file_id FROM videos_woman WHERE id = {id[0]}"""
        command = SELECT_VIDEO_WOMAN
        cursor.execute(command, id)
        return cursor

    def select_all_videos_man(self):
        SELECT_ALL_VIDEO = f"""SELECT * FROM videos_man"""
        command = SELECT_ALL_VIDEO
        cursor.execute(command)
        return cursor

    def select_all_videos_woman(self):
        SELECT_ALL_VIDEO = f"""SELECT * FROM videos_woman"""
        command = SELECT_ALL_VIDEO
        cursor.execute(command)
        return cursor


    def update_video_man(self, par):
        UPDATE_VIDEO_MAN = f"""UPDATE videos_man SET file_id = '{par[0]}' WHERE id = {par[1]}"""
        command = UPDATE_VIDEO_MAN
        cursor.execute(command, par)
        return cursor

    def update_video_woman(self, par):
        UPDATE_VIDEO_WOMAN = f"""UPDATE videos_woman SET file_id = '{par[0]}' WHERE id = {par[1]}"""
        command = UPDATE_VIDEO_WOMAN
        cursor.execute(command, par)
        return cursor



    def delete_messages(self):
        DELETE_MESSAGES_MAN = f"""DELETE FROM messages_man"""
        DELETE_MESSAGES_WOMAN = f"""DELETE FROM messages_woman"""
        cursor.execute(DELETE_MESSAGES_MAN)
        cursor.execute(DELETE_MESSAGES_WOMAN)


    def add_messages_man(self, message):
        ADD_MESSAGES_MAN = f"""INSERT INTO messages_man (id, message) VALUES ({message[0]}, '{message[1]}')"""
        command = ADD_MESSAGES_MAN
        cursor.execute(command, message)


    def add_messages_woman(self, message):
        ADD_MESSAGES_WOMAN = f"""INSERT INTO messages_woman (id, message) VALUES ({message[0]}, '{message[1]}')"""
        command = ADD_MESSAGES_WOMAN
        cursor.execute(command, message)


    def select_message_man(self, id):
        SELECT_MESSAGE_MAN = f"""SELECT message FROM messages_man WHERE id ={id[0]}"""
        command = SELECT_MESSAGE_MAN
        cursor.execute(command, id)
        return cursor


    def select_message_woman(self, id):
        SELECT_MESSAGE_WOMAN = f"""SELECT message FROM messages_woman WHERE id ={id[0]}"""
        command = SELECT_MESSAGE_WOMAN
        cursor.execute(command, id)
        return cursor


    def update_id_input(self, par):
        UPDATE_ID_INPUT = f"""UPDATE input SET id = {par[0]} WHERE username = '{par[1]}'"""
        command = UPDATE_ID_INPUT
        cursor.execute(command, par)


    def select_input(self, chatid):
        SELECT_INPUT = f"""SELECT * FROM input WHERE id = {chatid[0]}"""
        command = SELECT_INPUT
        cursor.execute(command, chatid)
        return cursor
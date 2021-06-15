from aiogram import types
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

def inline_url(text,url):
    inline_keyboard_url = InlineKeyboardMarkup(
        inline_keyboard=[
        [
            InlineKeyboardButton(text=text, url=url)
        ]
    ])
    return inline_keyboard_url

mg_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
        [
            InlineKeyboardButton(text='М', callback_data='man'),
            InlineKeyboardButton(text='Ж', callback_data='woman')
        ]
    ])

start_training = InlineKeyboardMarkup(
        inline_keyboard=[
        [
            InlineKeyboardButton(text='Начать тренировку', callback_data='start_training'),
        ]
    ])

done_man = InlineKeyboardMarkup(
        inline_keyboard=[
        [
            InlineKeyboardButton(text='Сделал', callback_data='done'),
        ]
    ])

done_woman = InlineKeyboardMarkup(
        inline_keyboard=[
        [
            InlineKeyboardButton(text='Сделала', callback_data='done'),
        ]
    ])

add_video_man_woman = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Видео для мужчин', callback_data='add_video_man')
        ],
        [
            InlineKeyboardButton(text='Видео для женщин', callback_data='add_video_woman')
        ],
        [
            InlineKeyboardButton(text='Видео для всех', callback_data='add_video_all')
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data=f'back')
        ]
    ])

add_video_id = InlineKeyboardMarkup(
    inline_keyboard=[

    ])
i=1
while i<10:
    add_video_id.add(InlineKeyboardButton(text=f'{i}', callback_data=f'video_{i}'))
    i+=1
add_video_id.add(InlineKeyboardButton(text="Назад", callback_data=f'back'))
from aiogram import executor

from handlers.mailing import mailing
from loader import dp, scheduler
import handlers

from utils import on_startup_notify


def schedule_jobs():
    scheduler.add_job(mailing, "cron", day_of_week='mon-sat', hour=9)
    #scheduler.add_job(mailing, "interval", minutes = 1)
async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)
    schedule_jobs()



if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
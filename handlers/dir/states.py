from aiogram.dispatcher.filters.state import State, StatesGroup

class TRAIN(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()
    step4 = State()
    step5 = State()
    step6 = State()
    step7 = State()
    step8 = State()
    step9 = State()
    step0 = State()

class ADD_VIDEO(StatesGroup):
    add_video = State()
    add_video_id_man = State()
    add_video_id_woman = State()


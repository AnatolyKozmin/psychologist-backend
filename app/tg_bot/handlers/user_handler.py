from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command 
from aiogram.types import Message


user_router = Router()

@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(text='...',
                         reply_markup=...)


@user_router.message(F.text.lower() == 'запись')
async def get_record(message: types.Message):
    await message.answer(text='линк')



@user_router.message(F.text.lower() == 'о нас')
async def get_record(message: types.Message):
    await message.answer(text='...')
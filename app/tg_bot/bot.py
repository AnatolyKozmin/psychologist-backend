import asyncio 
from aiogram import Bot, types, Dispatcher

from config import Settings
from handlers.user_handler import user_router


bot = Bot(token=Settings.BOT_TOKEN)

dp = Dispatcher(bot)
dp.include_router(user_router)



async def main():
    print("Запущен")

    bot.delete_webhook(drop_pending_updates=True)
    dp.start_polling(bot)

asyncio.run(main())
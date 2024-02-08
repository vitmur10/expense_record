from Const import *



@dp.message_handler(commands=['start'])
async def hello(message: aiogram.types.Message):
    pass
if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)

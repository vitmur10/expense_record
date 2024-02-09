from Const import *
from keybord import *


@dp.message_handler(commands=['start'])
async def hello(message: aiogram.types.Message):
    """command start"""
    await message.answer(cfg['welcome_message'], reply_markup=keyboard)


# Обробник клавіш з інлайн клавіатури
@dp.callback_query_handler(lambda c: c.data.startswith('category_'))
async def process_callback(callback_query: aiogram.types.CallbackQuery):
    category = callback_query.data.split('_')[1]
    await bot.send_message(callback_query.from_user.id, f"Ви обрали категорію: {category}")


@dp.message_handler(content_types=['text'])
async def text(message: aiogram.types.Message):
    await message.answer("Оберіть категорію витрат:", reply_markup=inline_keyboard)


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)

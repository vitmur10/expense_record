from aiogram.dispatcher.filters import state

from Const import *
from keybord import *
from statistic import *
from aiogram.dispatcher.filters.state import State, StatesGroup


class Add_cost(StatesGroup):
    category = State()  # State to store the text of the answer
    s = State()  # State to store the user ID


@dp.callback_query_handler(state=Add_cost.category)
async def process_callback_state(callback_query: aiogram.types.CallbackQuery):
    async with state.proxy() as data:
        data['category'] = callback_query.data.split('_')[1]
    await bot.send_message(callback_query.from_user.id, f"Напишіть суму")
    await Add_cost.next()

@dp.message_handler(state=Add_cost.s)
async def add_most_frequently_asked_questions_faculty(message: aiogram.types.Message,
                                                      state: aiogram.dispatcher.FSMContext):
    """Add to FAQ with a button"""
    async with state.proxy() as data:
        data['s'] = message.text
    await state.finish()
    await message.answer(f"{data['category'], data['s']}")
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
    if "Категорії" == message.text:
        await message.answer("\n".join(categories))
    elif 'Додати витрату' == message.text:
        await message.answer('Виберіть категорію і напишіть суму', reply_markup=inline_keyboard)
        await Add_cost.category.set()
    elif 'Переглянути витрати' == message.text:
        await message.answer("Оберіть категорію витрат:", reply_markup=inline_keyboard)
    elif 'Додати категорію' == message.text:
        await message.answer("Напишіть категорію")
        categories.append(message.text)


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)

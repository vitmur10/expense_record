import datetime

from aiogram.dispatcher.filters import state

from Const import *
from keybord import *
from statistic import *
from aiogram.dispatcher.filters.state import State, StatesGroup


class Add_cost(StatesGroup):
    category = State()
    s = State()
    comment = State()


@dp.callback_query_handler(state=Add_cost.category)
async def process_callback_state(callback_query: aiogram.types.CallbackQuery, state: aiogram.dispatcher.FSMContext):
    async with state.proxy() as data:
        data['category'] = callback_query.data.split('_')[1]
    await bot.send_message(callback_query.from_user.id, "Напишіть суму")
    await Add_cost.next()


@dp.message_handler(state=Add_cost.s, content_types=['text'])
async def add_most_frequently_asked_questions_faculty(message: aiogram.types.Message,
                                                      state: aiogram.dispatcher.FSMContext):
    """Add to FAQ with a button"""
    async with state.proxy() as data:
        data['s'] = message.text
    await bot.send_message(message.from_user.id, "Напишіть коментар")
    await Add_cost.next()



@dp.message_handler(state=Add_cost.comment, content_types=['text'])
async def add_most_frequently_asked_questions_faculty(message: aiogram.types.Message,
                                                      state: aiogram.dispatcher.FSMContext):
    """Add to FAQ with a button"""
    async with state.proxy() as data:
        data['comment'] = message.text


    # SQL-запит для додавання даних
    insert_query = '''
    INSERT INTO records (category, comment, data, suma)
    VALUES (?, ?, ?, ?)
    '''

    # Виконання SQL-запиту для додавання даних
    cur.execute(insert_query, (data['category'], data['comment'], datetime.datetime.now().date(), data['s']))

    # Підтвердження виконання запиту та збереження змін
    con.commit()

    # Закриття з'єднання з базою даних

    await state.finish()
    await message.answer(f" Додано витрату на суму {data['s'][0:]} у категорію - {data['category'][0:]}\n{ data['comment'][0:] }")

@dp.message_handler(commands=['start'])
async def hello(message: aiogram.types.Message):
    """command start"""
    await message.answer(cfg['welcome_message'], reply_markup=keyboard)


# Обробник клавіш з інлайн клавіатури
@dp.callback_query_handler(lambda c: c.data.startswith('category_'))
async def process_callback(callback_query: aiogram.types.CallbackQuery):
    category = callback_query.data.split('_')[1]
    await bot.send_message(callback_query.from_user.id, f"Витрати: {category}\n"
                                                        f"Сума {sum(send_costs(category=category[2:]).values())}\n"
                                                        f"{send_costs(category=category[2:])}")


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

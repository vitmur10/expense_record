from Const import *

keyboard = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)

add_cost = aiogram.types.KeyboardButton(cfg['add_cost'])
view_costs = aiogram.types.KeyboardButton(cfg['view_costs'])
category = aiogram.types.KeyboardButton(cfg['category'])
add_category = aiogram.types.KeyboardButton(cfg['add_category'])

keyboard.add(add_cost, category).add(view_costs, add_category)

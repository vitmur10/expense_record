import aiogram.types

from Const import *

keyboard = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)

add_cost = aiogram.types.KeyboardButton(cfg['add_cost'])
view_costs = aiogram.types.KeyboardButton(cfg['view_costs'])
category = aiogram.types.KeyboardButton(cfg['category'])
add_category = aiogram.types.KeyboardButton(cfg['add_category'])
view_statistics = aiogram.types.KeyboardButton(cfg['view_statistics'])
delete_cost = aiogram.types.KeyboardButton(cfg['delete_cost'])

keyboard.add(add_cost, category).add(view_costs, add_category)
keyboard.add(view_statistics, delete_cost)
inline_keyboard = aiogram.types.InlineKeyboardMarkup(row_width=2)
buttons = [aiogram.types.InlineKeyboardButton(text=c, callback_data=f"category_{c}") for c in categories]
inline_keyboard.add(*buttons)

delete_category_keyboard = aiogram.types.InlineKeyboardMarkup(row_width=2)
buttons = [aiogram.types.InlineKeyboardButton(text=d, callback_data=f"delete_{d}") for d in categories]
delete_category_keyboard.add(*buttons)

delete_cost = aiogram.types.InlineKeyboardMarkup(row_width=1)

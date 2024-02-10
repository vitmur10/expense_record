from Const import *

keyboard = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)

add_cost = aiogram.types.KeyboardButton(cfg['add_cost'])
view_costs = aiogram.types.KeyboardButton(cfg['view_costs'])
category = aiogram.types.KeyboardButton(cfg['category'])
add_category = aiogram.types.KeyboardButton(cfg['add_category'])

keyboard.add(add_cost, category).add(view_costs, add_category)
inline_keyboard = aiogram.types.InlineKeyboardMarkup(row_width=2)
buttons = [aiogram.types.InlineKeyboardButton(text=c, callback_data=f"category_{c}") for c in categories]
inline_keyboard.add(*buttons)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn.add(KeyboardButton("📲 Telefon raqamni yuborish", request_contact=True))

btn2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn2.add(KeyboardButton("❌ Yo'q"))




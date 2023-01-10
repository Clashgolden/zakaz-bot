from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from states.first import First
from keyboards.default.telefon import btn,btn2
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import contact

from loader import dp,bot


@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum👋, Botdan foydalanish uchun Ro'yxatdan o'tishinggiz lozim❗️\n\n<b>Marhamat qilib isminggizni kiriting...❓</b>")
    await First.ism.set()

@dp.message_handler(state=First.ism)
async def bir(message:types.Message, state:FSMContext):
    ism = message.text
    await state.update_data({
        'ism' : ism
    })
    text = f"<b>✅Isminggizni qabul qildim endi,\n\n📱Telefon raqaminggizni yuboring...❓</b>"
    await message.answer(text,reply_markup=btn)
    await First.next()

@dp.message_handler(state=First.Telefon,content_types=['contact'])
async def ikki(message:types.Message, state=FSMContext):
    Telefon = message.contact.phone_number
    await state.update_data({
        'Telefon' : Telefon
    })
    text = f"✅Telefon raqaminggiz qabul qilindi. \n\n<b>Endi har ehtimolga qarshi qo'shimcha telefon raqaminggizni yozing. Agar qo'shimcha raqam mavjud bo'lmasa pastdagi - ❌Yo'q tugmasini bosing</b>"
    await message.answer(text,reply_markup=btn2)
    await First.next()

@dp.message_handler(state=First.dopalnitelniy)
async def uch(message:types.Message, state:FSMContext):
    dopalnitelniy = message.text
    await state.update_data({
        'dopalnitelniy' : dopalnitelniy
    })
    text = f"✅Qabul qilindi.\n\n<b>Marhamat qilib bizni qayerdan topganinggizni yozib qoldirsanggiz ❓</b>"
    await message.answer(text)
    await First.next()

@dp.message_handler(state=First.qayer)
async def tort(message:types.Message, state:FSMContext):
    qayer = message.text
    await state.update_data({
        'qayer':qayer
    })
    text = f"Rahmat❗  Ma'lumotlaringgiz qabul qilindi✅\n\n<b>Menejerlarimiz siz bilan tez orada bog'lanishadi❗\n\nAgar sizda qanaqadir savollar bo'lsa\nbizga murojaat qiling: +998 90 559 07 47</b>"
    await message.answer(text)
    data = await state.get_data()
    result = f"Yangi Foydalanuvhchi:\n\n"\
             f"Ismi: <b>  {data['ism']}</b>\n"\
             f"Raqami: <b>  {data['Telefon']}</b>\n" \
             f"Qo'shimcha: <b>  {data['dopalnitelniy']}</b>\n"\
             f"Qayerdan Topgan: <b>  {data['qayer']}</b>"
    await bot.send_message(chat_id=-1001474410433, text=result)
    await state.finish()
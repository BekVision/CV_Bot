from aiogram import Bot, Dispatcher,types, F, Router
from aiogram.filters import Command, CommandStart
import asyncio
from aiogram.methods import send_message
from aiogram.types import InputMediaPhoto, BotCommand, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InputFile, FSInputFile, Message, CallbackQuery
from keyboard import main_menu, portfolio_keyboard, skills_keyboard
from ai import get_ai_response
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


# Bot API TOKEN
API_TOKEN = "7549195361:AAEEril3nMFa5yyneCftUhRVefFehIu-TQ8"
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
router = Router()


# Add in bot menu
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запустить бота"),
        BotCommand(command="/help", description="Помощь"),
    ]
    await bot.set_my_commands(commands)


# When bot start
async def on_startup(dispatcher: Dispatcher):
    await bot.send_message(chat_id="5078835259", text="Bot ishga tushdi.")

# When sent /start
@dp.message(Command("start"))
async def menu_handler(message: types.Message):
    await message.answer(
        text="Salom! 👋\n\nMen *Asadbek Ashurov* – *Python backend* dasturchisiman.\n\nBu bot orqali men haqimdagi ma'lumotlarni, portfoliyolarimni va bog‘lanish usullarini ko‘rishingiz mumkin.",
        parse_mode="Markdown",
        reply_markup=main_menu()
)


# About me
@dp.message(F.text == "👨‍💻 Men haqimda")
async def about_me(message: types.Message):
    await message.answer(
        text="🧑 Ism: *Asadbek Ashurov* \n\n🎓 Ta’lim: *PDP University, Software Development* yo‘nalishi \n\n📍 Manzil: *Toshkent, O‘zbekiston* \n\n💼 Maqsad: *Python Backend* dasturchi sifatida IT sohasida ishlash \n\n📅 Tajriba: *1+ yil* amaliy mashg‘ulotlar va loyihalar bilan",
        parse_mode="Markdown"
)

# Connect
@dp.message(F.text == "📞 Bog‘lanish")
async def connect(message: types.Message):
    await message.answer(
        text="📧 Email: asadbekashurov858@gmail.com \n\n💬 Telegram: @BekDevSoft \n\n🌐 GitHub: github.com/BekVision \n\n📱 Phone number: +998 95 885 89 82"
)


# Portfolio
@router.message(F.text == "📂 Portfolio")
async def portfolio(message: types.Message):
    await message.answer(
        text="📁 Portfolio loyihalarim: \n\n1. 🧾 Avtoservis menejment bot – Telegram orqali mashina ta’mirlash jarayonini boshqarish (Python + SQLite). \n\n2. 💼 Ish topish platformasi – Django asosida yosh mutaxassislar uchun platforma. \n\n3. ♟ Shaxmat o‘yini – Python va Tkinter yordamida oddiy grafikli shaxmat dasturi. \n\n🔗 GitHub sahifam: github.com/BekVision",
        reply_markup=portfolio_keyboard())

# Send my CV
@dp.callback_query(F.data == "CV")
async def send_cv(callback_query: types.CallbackQuery):
    file_path = "Ashurov_Asadbek_CV.pdf"

    # Faylni to‘g‘ri ochish uchun FSInputFile sinfidan foydalanamiz
    doc = FSInputFile(path=file_path, filename="Ashurov_Asadbek_CV.pdf")

    await callback_query.message.answer_document(document=doc, caption="My CV 📄")
    await callback_query.answer()



# Courses
@router.message(F.text == "🧑‍🎓 O‘qigan kurslarim")
async def portfolio(message: types.Message):
    await message.answer(
        text="📚 Tugallangan kurslar:\n\n- Python Dasturlash Asoslari – PDP University \n\n- Django Web Development – Udemy \n\n- Git & GitHub asoslari – YouTube / Amaliy mashg‘ulotlar",
    )


# Skills
@router.message(F.text == "🛠 Skilllarim")
async def portfolio(message: types.Message):
    await message.answer(
        text="🔧Quidagi texnologiyalar bo'yicha bilimga egaman:",
        reply_markup=skills_keyboard()
)


Python = """
🐍 Python — bu zamonaviy, o‘qilishi oson va kuchli dasturlash tili.\n\n
💡 Uni yordamida veb-ilovalar, Telegram botlar, sun’iy intellekt, avtomatlashtirish va ko‘plab boshqa tizimlar yaratish mumkin.\n\n
🔧 Men Python'da OOP, async, fayl ishlovlari, ma'lumotlar bazasi, API bilan ishlash bo‘yicha chuqur bilimga egaman.\n\n
"""

Javascript = """
💻 JavaScript — bu veb sahifalarni interaktiv qilish uchun ishlatiladigan til.\n\n
🌐 Uni yordamida tugma bosish, forma to‘ldirish, slayderlar kabi dinamik effektlar qo‘shiladi.\n\n
📌 Men JavaScript asoslarini bilaman va Frontendni tushunishim menga backend bilan yaxshiroq integratsiya qilishga yordam beradi.\n\n
"""

C_plus_plus = """
⚙️ C++ — bu yuqori samaradorlikka ega tizimli dasturlash tili.\n\n
🚀 Uni yordamida o‘yinlar, tizim dasturlari, haydovchilar (drivers) va murakkab hisob-kitoblar qilinadigan ilovalar ishlab chiqiladi.\n\n
🧠 Men C++ orqali dasturlash mantig‘ini chuqur tushunganman va bu menga boshqa tillarda samarali ishlashga yordam beradi.\n\n
"""

Sql = """
🗃 SQL (Structured Query Language) — bu ma’lumotlar bazasidagi ma’lumotlarni yaratish, o‘zgartirish va olish uchun ishlatiladi.\n\n
📊 Men SQL orqali ma’lumotlar ustida CRUD (Create, Read, Update, Delete) amallarini bajarishni, JOINlar, GROUP BY, subquery'larni ishlatishni bilaman.\n\n
🔌 Django va Python'da bazaga ulanish tajribam bor.\n\n
"""

Django = """
🌐 Django — bu kuchli va xavfsiz Python web-framework.\n\n
🚧 U yordamida web-saytlar, admin panel, login tizimi, ma’lumotlar bazasi bilan ishlaydigan ilovalar yaratiladi.\n\n
⚡ Men Django’da loyihalar yaratganman: CRUD funksiyalar, foydalanuvchi autentifikatsiyasi, REST API, admin panelni sozlash bo‘yicha tajribam bor.\n\n
"""

FastAPI = """
⚡ FastAPI — bu Python uchun zamonaviy, tezkor va yengil web API framework.\n\n
🚀 U yordamida tez ishlaydigan backend ilovalar va RESTful API lar yaratish mumkin.\n\n
🧩 Men FastAPI orqali oddiy va murakkab endpointlar yaratishni, JSON bilan ishlashni va autentifikatsiyani qilganman.\n\n
"""

@dp.callback_query()
async def skills(callback: types.CallbackQuery):
    if callback.data == "Python":
        await callback.message.answer(Python)
    elif callback.data == "Javascript":
        await callback.message.answer(Javascript)
    elif callback.data == "C++":
        await callback.message.answer(C_plus_plus)
    elif callback.data == "SQL":
        await callback.message.answer(Sql)
    elif callback.data == "Django":
        await callback.message.answer(Django)
    elif callback.data == "FastAPI":
        await callback.message.answer(FastAPI)
    else:
        await callback.answer("Ma'lumotlar topilmadi")





# # AI Assistant
# @router.message(F.text == "AI Assistant")
# async def portfolio(message: types.Message):
#     await message.answer(
#         text="AI",
#         reply_markup=skills_keyboard()
# )
#
# @dp.message(F.text)
# async def ai_response(message: Message):
#     user_message = message.text
#
#     # AI javobini olish
#     ai_reply = await get_ai_response(user_message)
#
#     # Javobni yuborish
#     await message.answer(ai_reply)



# Main
async def main():
    # Menu
    await set_commands(bot)

    dp.startup.register(on_startup)
    dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
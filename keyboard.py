from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# Main buttons
def main_menu():
    button = KeyboardButton(text="👨‍💻 Men haqimda")
    button2 = KeyboardButton(text="📂 Portfolio")
    button3 = KeyboardButton(text="🧑‍🎓 O‘qigan kurslarim")
    button4 = KeyboardButton(text="🛠 Skilllarim")
    button5 = KeyboardButton(text="📞 Bog‘lanish")
    button6 = KeyboardButton(text="AI Assistant")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3],
            [button4, button5],
            [button6]
        ],
        resize_keyboard=True
    )
    return rkm

def portfolio_keyboard():
    button = InlineKeyboardButton(text="📄 CV", callback_data="CV")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button]
        ]
    )
    return ikm


def skills_keyboard():
    button = InlineKeyboardButton(text="Python", callback_data="Python")
    button1 = InlineKeyboardButton(text="Javascript", callback_data="Javascript")
    button2 = InlineKeyboardButton(text="C++", callback_data="C++")
    button3 = InlineKeyboardButton(text="SQL", callback_data="SQL")
    button4 = InlineKeyboardButton(text="Django", callback_data="Django")
    button5 = InlineKeyboardButton(text="FastAPI", callback_data="FastAPI")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button],
            [button1],
            [button2],
            [button3],
            [button4],
            [button5]
        ]
    )
    return ikm

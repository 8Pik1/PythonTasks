import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.filters import Command
import asyncio

API_TOKEN = '7860779088:AAFO7Fix4bdpMhG_Pb8tgonKk3IFVy87ld0'

# Настройка бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Запуск бота
async def on_start():
    # Вместо executor.start_polling используем start_polling()
    await dp.start_polling(bot)


FILES = {
    "bb_male_1": "./trainings/до_1_года.xlsx",
    "bb_male_2": "./trainings/1_-_3_года.xlsx",
    "bb_male_3": "./trainings/более_3_лет.xlsx",
    "pl_male_1": "./trainings/до_1_года.xlsx",
    "pl_male_2": "./trainings/1_-_3_года.xlsx",
    "pl_male_3": "./trainings/более_3_лет.xlsx",
}

# Главное меню
menu_data = {
    "main": {
        "text": "💪 Добро пожаловать! Выберите тренировку для себя:",
        "buttons": [
            ("🦍 Пауэрлифтинг", "powerlifting"),
            ("🏆 Бодибилдинг", "bodybuilding"),
        ],
    },
    "powerlifting": {
        "text": "🦍 Пауэрлифтинг: Выберите ваш опыт:",
        "buttons": [
            ("🐣 До 1 года", "pl_male_1"),
            ("📈 1 - 3 года", "pl_male_2"),
            ("💀 Более 3 лет", "pl_male_3"),
            ("🔙 Назад", "main"),
        ],
    },
    "bodybuilding": {
        "text": "🏆 Бодибилдинг: Выберите ваш опыт:",
        "buttons": [
            ("🐣 До 1 года", "bb_male_1"),
            ("📈 1 - 3 года", "bb_male_2"),
            ("💀 Более 3 лет", "bb_male_3"),
            ("🔙 Назад", "main"),
        ],
    },
}

# Логирование ошибок
logging.basicConfig(level=logging.INFO)

# Отправка клавиатуры
def get_keyboard(menu_key):
    buttons = [types.InlineKeyboardButton(text=text, callback_data=data) for text, data in menu_data[menu_key]["buttons"]]
    return types.InlineKeyboardMarkup(row_width=2,inline_keyboard=[buttons])

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(menu_data["main"]["text"], reply_markup=get_keyboard("main"))

# Обработчик нажатий на кнопки
@dp.callback_query()
async def process_menu(callback_query: types.CallbackQuery):
    data = callback_query.data
    print("012")
    # Если выбран пункт из главного меню
    if data == "main":
        await bot.send_message(callback_query.from_user.id, menu_data["main"]["text"], reply_markup=get_keyboard("main"))

    elif data == "powerlifting":
        await bot.send_message(callback_query.from_user.id, menu_data["powerlifting"]["text"], reply_markup=get_keyboard("powerlifting"))

    # Если выбран пункт из "Пауэрлифтинга"
    elif data.startswith("pl_"):
        print("123")
        await bot.send_message(callback_query.from_user.id, menu_data["powerlifting"]["text"], reply_markup=get_keyboard("powerlifting"))

    # Если выбран пункт из "Бодибилдинга"
    elif data.startswith("bb_"):
        await bot.send_message(callback_query.from_user.id, menu_data["bodybuilding"]["text"], reply_markup=get_keyboard("bodybuilding"))

    # Если выбран опыт для Пауэрлифтинга или Бодибилдинга
    elif data in FILES:
        await bot.send_message(callback_query.from_user.id, "Вот ваш тренировочный план:")
        file_path = FILES[data]
        file = InputFile(file_path)
        await bot.send_document(callback_query.from_user.id, file)

    # Обработка кнопки "Назад"
    elif data == "main":
        await bot.send_message(callback_query.from_user.id, menu_data["main"]["text"], reply_markup=get_keyboard("main"))

    else:
        await bot.send_message(callback_query.from_user.id, "неизвестная команда: " + data)
# Регистрация хендлеров
#dp.register_message_handler(start, commands="start")

#dp.register_callback_query_handler(process_menu)


if __name__ == "__main__":
    # Используем asyncio.run для запуска бота
    asyncio.run(on_start())

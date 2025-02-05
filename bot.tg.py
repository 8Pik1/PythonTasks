from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

TOKEN = "8047778137:AAHUhKdMTxhbx1wckFat5W4Oaa3X-vv3XgU"  # Вставь сюда свой токен

# Структура меню
menu_data = {
    "main": {
        "text": "💪 Добро пожаловать!\n"
                "\n"
                "Выберите тренировку для себя:",
        "buttons": [
            ("🦍 Пауэрлифтинг", "menu_1"),
            ("🏆 Бодибилдинг", "menu_2"),
            ("ℹ️ Дополнительная информация", "about"),
        ],
    },
    "menu_1": {
        "text": "🦍 Пауэрлифтинг\n"
                "\n"
                "⚠️ Для женщин подходит только начальный и средний уровень.",
        "buttons": [
            ("🐣 Начальный", "sub_1_1"),
            ("📈 Средний", "sub_1_2"),
            ("💀 Высокий", "sub_1_3"),
            ("🔙 Назад", "main"),
        ],
    },
    "menu_2": {
        "text": "🏆 Бодибилдинг\n"
                "\n"
                "Выберите ваш пол:",
        "buttons": [
            ("🧑 Мужчина", "bb_male"),
            ("👩 Женщина", "bb_female"),
            ("🔙 Назад", "main"),
        ],
    },
    # Выбор стажа для мужчин
    "bb_male": {
        "text": "🏆 Бодибилдинг\n"
                "\n"
                "📅 Выберите ваш стаж:",
        "buttons": [
            ("🐣 Менее 1 года", "bb_male_1"),
            ("📈 1-3 года", "bb_male_2"),
            ("💀 Более 3 лет", "bb_male_3"),
            ("🔙 Назад", "menu_2"),
        ],
    },
    # Выбор стажа для женщин
    "bb_female": {
        "text": "🏆 Бодибилдинг\n"
                "\n"
                "📅 Выберите ваш стаж:",
        "buttons": [
            ("🐣 Менее 1 года", "bb_female_1"),
            ("📈 1-3 года", "bb_female_2"),
            ("💀 Более 3 лет", "bb_female_3"),
            ("🔙 Назад", "menu_2"),
        ],
    },
    # Уровни тренировок
    "bb_male_1": {
        "text": "🏆 Бодибилдинг - Стаж: 🐣 Менее 1 года\n"
                "\n"
                "Приятной тренировки! ✅",
        "buttons": [
            ("🔙 Назад", "bb_male"),
        ],
    },
    "bb_male_2": {
        "text": "🏆 Бодибилдинг - Стаж: 📈 1-3 года\n"
                "\n"
                "Приятной тренировки! ✅",
        "buttons": [
            ("🔙 Назад", "bb_male"),
        ],
    },
    "bb_male_3": {
        "text": "🏆 Бодибилдинг - Стаж: 💀 Более 3 лет\n"
                "\n"
                "Приятной тренировки! ✅",
        "buttons": [
            ("🔙 Назад", "bb_male"),
        ],
    },
    "bb_female_1": {
        "text": "🏆 Бодибилдинг - Стаж: 🐣 Менее 1 года\n"
                "\n"
                "Приятной тренировки! ✅",
        "buttons": [
            ("🔙 Назад", "bb_female"),
        ],
    },
    "bb_female_2": {
        "text": "🏆 Бодибилдинг - Стаж: 📈 1-3 года\n"
                "\n"
                "Приятной тренировки! ✅",
        "buttons": [
            ("🔙 Назад", "bb_female"),
        ],
    },
    "bb_female_3": {
        "text": "🏆 Бодибилдинг - Стаж: 💀 Более 3 лет\n"
                "\n"
                "Приятной тренировки! ✅",
        "buttons": [
            ("🔙 Назад", "bb_female"),
        ],
    },
    "about": {
        "text": "ℹ️ Мы — команда разработчиков Telegram-ботов!\n"
                "\n"
                "💡 Здесь можно найти информацию о тренировках.",
        "buttons": [
            ("🔙 Назад", "main"),
        ],
    },
}

# Функция для рендера кнопок
def get_menu(menu_name):
    menu = menu_data.get(menu_name, menu_data["main"])
    keyboard = [[InlineKeyboardButton(text, callback_data=callback)] for text, callback in menu["buttons"]]
    return menu["text"], InlineKeyboardMarkup(keyboard)

# Команда /start (автоматический запуск меню)
async def start(update: Update, context):
    text, reply_markup = get_menu("main")
    await update.message.reply_text(text, reply_markup=reply_markup)

# Автоматический запуск меню при первом сообщении (даже если человек просто написал боту)
async def auto_start(update: Update, context):
    text, reply_markup = get_menu("main")
    await update.message.reply_text(text, reply_markup=reply_markup)

# Обработчик нажатий на кнопки
async def menu_handler(update: Update, context):
    query = update.callback_query
    await query.answer()

    menu_name = query.data
    text, reply_markup = get_menu(menu_name)
    await query.message.edit_text(text, reply_markup=reply_markup)

# Основная функция
def main():
    app = Application.builder().token(TOKEN).build()

    # Обработчики команд и сообщений
    app.add_handler(CommandHandler("start", start))  # /start
    app.add_handler(CallbackQueryHandler(menu_handler))  # Нажатия на кнопки
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_start))  # Если человек просто написал

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()


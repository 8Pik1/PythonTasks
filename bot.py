import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

# Стикеры для мужчин и женщин
male_sticker = 'CAACAgIAAxkBAAIBfmZ0Vq0sKyflLrr9-p9ktg7bVvmKBwAC6wADUv6SBXq6VHLdZaE3KgQ'
female_sticker = 'CAACAgIAAxkBAAIBfGZ0VnV0gprz1B1tLlAmgU3jZsLU4wACSwADUv6SBXq6VHLdZexqKgQ'

# Вставьте свой токен
TOKEN = "8047778137:AAHUhKdMTxhbx1wckFat5W4Oaa3X-vv3XgU"


# Функции для обработки команд
async def start(update, context):
    # Создаём кнопки для выбора тренировки
    keyboard = [
        [
            InlineKeyboardButton("Паверлифтинг", callback_data='powerlifting'),
            InlineKeyboardButton("Силовой бодибилдинг", callback_data='bodybuilding')
        ],
        [InlineKeyboardButton("Тренировка для восстановления", callback_data='recovery')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    message = await update.message.reply_text('Выберите тип тренировки:', reply_markup=reply_markup)

    # Сохраняем сообщение для редактирования (в дальнейшем удалим)
    context.user_data['message_id'] = message.message_id

    # Запрос пола пользователя в виде кнопок
    gender_keyboard = [
        [
            InlineKeyboardButton("Мужчина", callback_data='male'),
            InlineKeyboardButton("Женщина", callback_data='female')
        ]
    ]
    gender_reply_markup = InlineKeyboardMarkup(gender_keyboard)
    await update.message.reply_text('Выберите ваш пол:', reply_markup=gender_reply_markup)


async def button(update, context):
    query = update.callback_query
    await query.answer()

    # Удаление первого сообщения (выбор тренировки) после ответа
    if 'message_id' in context.user_data:
        await query.message.chat.delete_message(message_id=context.user_data['message_id'])

    if query.data == "powerlifting":
        await query.edit_message_text(text="Вы выбрали Паверлифтинг!")
    elif query.data == "bodybuilding":
        await query.edit_message_text(text="Вы выбрали Силовой бодибилдинг!")
    elif query.data == "recovery":
        await query.edit_message_text(text="Вы выбрали тренировку для восстановления!")

    # Теперь покажем следующий выбор для пола
    if query.data == "male":
        await query.message.reply_text(text="Вы выбрали пол: Мужчина")
        await query.message.reply_sticker(male_sticker)
    elif query.data == "female":
        await query.message.reply_text(text="Вы выбрали пол: Женщина")
        await query.message.reply_sticker(female_sticker)


# Запуск бота
async def main():
    # Создание объекта Application
    application = Application.builder().token(TOKEN).build()

    # Регистрируем команды
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Запуск бота
    await application.run_polling()


if __name__ == '__main__':
    # Заменяем asyncio.run() на работу с текущим циклом событий
    import nest_asyncio

    nest_asyncio.apply()  # Это позволяет работать с асинхронным циклом в уже работающем приложении

    asyncio.get_event_loop().run_until_complete(main())  # Запуск бота

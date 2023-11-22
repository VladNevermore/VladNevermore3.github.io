from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Токен вашего бота, полученный от @BotFather в Telegram
TOKEN = "6876546786:AAEvKWFkgOHjX_f8hGzc9TUTwpyULJ0rhaQ"

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr"Привет {user.mention_markdown_v2()} хочешь получить больше информации о нашей кальянной? Тогда тебе сюда!",
        reply_markup=telegram.ReplyKeyboardMarkup(
            [[telegram.KeyboardButton("Посмотреть меню", url="t.me/Hifort_bot/TestCWebApp")]]
        ),
    )

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()

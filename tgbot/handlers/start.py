from telebot import TeleBot


def send_welcome(message, bot: TeleBot):
    bot.send_message(
        message.chat.id,
        "Greetings! I'll be glad to help you not to miss anything important. Enter `/help` to see more info.",
    )

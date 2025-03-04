# ruff: noqa: F401

from telebot import TeleBot

from .forget import forget_webiste
from .help import send_help
from .start import send_welcome
from .watch import watch_website


def register_handlers(bot: TeleBot):
    bot.message_handler(commands=["start"])(lambda message: send_welcome(message, bot))
    bot.message_handler(commands=["help"])(lambda message: send_help(message, bot))
    bot.message_handler(commands=["watch"])(lambda message: watch_website(message, bot))
    bot.message_handler(commands=["forget"])(
        lambda message: forget_webiste(message, bot)
    )

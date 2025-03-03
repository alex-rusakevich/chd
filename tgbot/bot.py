import multiprocessing

import telebot
from django.conf import settings

bot = telebot.TeleBot(
    settings.BOT_TOKEN,
    skip_pending=True,
    parse_mode="Markdown",
    threaded=True,
    num_threads=multiprocessing.cpu_count(),
)

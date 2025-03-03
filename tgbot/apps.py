import time

from django.apps import AppConfig

from tgbot import TG_WEBHOOK_URL
from tgbot.bot import bot


class TgbotConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tgbot"

    def ready(self):
        bot.remove_webhook()
        time.sleep(1)

        bot.set_webhook(
            url=TG_WEBHOOK_URL,
            drop_pending_updates=True,
        )

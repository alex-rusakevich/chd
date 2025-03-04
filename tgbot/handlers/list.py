from telebot import TeleBot

from checker.models import WatchedWebsite


def list_webistes(message, bot: TeleBot):
    websites = WatchedWebsite.objects.filter(chat_id=message.chat.id)

    bot.send_message(message.chat.id, "\n".join(ws.website_url for ws in websites))

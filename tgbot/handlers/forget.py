from telebot import TeleBot

from checker.models import WatchedWebsite


def forget_webiste(message, bot: TeleBot):
    message_parts = message.text.split(" ", 1)

    if len(message_parts) != 2:
        bot.send_message(
            message.chat.id,
            "Wrong command syntax, see `/help`",
        )
        return

    website_url = message_parts[1]

    ws = WatchedWebsite.objects.filter(website_url=website_url)

    if ws.count() == 0:
        bot.send_message(
            message.chat.id,
            "The website matching query does not exist",
        )
        return

    ws.delete()

    bot.send_message(
        message.chat.id,
        "The website {} has been forgotten successfully".format(website_url),
    )

from checker.tasks import add_watched_website


def watch_website(message, bot):
    message_parts = message.text.split(" ", 1)

    if len(message_parts) != 2:
        bot.send_message(
            message.chat.id,
            "Wrong command syntax, see `/help`",
        )
        return

    website_url = message_parts[1]

    bot.send_message(
        message.chat.id,
        "Your website `{}` has been queued to be added".format(website_url),
    )

    add_watched_website.delay(message.chat.id, website_url)

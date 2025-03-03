from checker.tasks import add_watched_website
from tgbot.bot import bot


@bot.message_handler(commands=["watch"])
def watch_website(message):
    website_url = message.text.split(" ", 1)[1]

    bot.send_message(
        message.chat.id,
        "Your website `{}` has been queued to be added".format(website_url),
    )

    add_watched_website.delay(message.chat.id, website_url)

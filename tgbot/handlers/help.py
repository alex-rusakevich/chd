from django.conf import settings
from telebot import TeleBot


def send_help(message, bot: TeleBot):
    bot.send_message(
        message.chat.id,
        """
`/help` — see this message
`/watch site` — watch the site's changes (max {max_watched} websites)
`/list` ­— see your watched websites list
`/forget site` — forget about the site
        """.format(max_watched=settings.MAX_WATCHED_PER_USER).strip(),
    )

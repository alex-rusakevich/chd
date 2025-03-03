import hashlib

import requests
import ua_generator
from celery import shared_task
from django.conf import settings

from checker.models import WatchedWebsite
from tgbot.bot import bot


@shared_task
def add_watched_website(chat_id, website_url: str):
    website_url = website_url.lower()

    if not website_url.startswith("http"):
        website_url = "https://" + website_url

    ua = ua_generator.generate()

    website_content = requests.get(website_url, headers=ua.headers.get()).content
    website_hash = hashlib.sha256(website_content).hexdigest()

    watched_of_user = WatchedWebsite.objects.filter(chat_id=chat_id)

    # region Quota checks
    if watched_of_user.count() >= settings.MAX_WATCHED_PER_USER:
        bot.send_message(
            chat_id,
            "Only `{}` watched websites are allowed per user".format(
                settings.MAX_WATCHED_PER_USER
            ),
        )

        return

    if watched_of_user.filter(website_url=website_url).count() >= 1:
        bot.send_message(
            chat_id,
            "You watch the website `{}` already".format(website_url),
        )

        return
    # endregion

    WatchedWebsite.objects.create(
        chat_id=chat_id, website_url=website_url, website_hash=website_hash
    )

    bot.send_message(
        chat_id,
        "Your website `{}` has been added".format(website_url),
    )

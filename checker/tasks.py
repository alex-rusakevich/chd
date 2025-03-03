import random
import time
from logging import getLogger

from celery import group, shared_task
from django.conf import settings

from chd.celery import app
from checker.models import WatchedWebsite
from checker.utils import get_website_hash
from tgbot.bot import bot

logger = getLogger(__name__)


def _add_watched_website(chat_id, website_url: str):
    website_hash = get_website_hash(website_url)

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


@shared_task
def add_watched_website(chat_id, website_url: str):
    bot.send_chat_action(chat_id, "typing")

    try:
        _add_watched_website(chat_id, website_url)
    except Exception as e:
        bot.send_message(
            chat_id,
            "An error occurred. Check if your site exists and is available and try again later",
        )
        logger.exception(e)
    else:
        bot.send_message(
            chat_id,
            "Your website `{}` has been added".format(website_url),
        )


@app.task
def check_website_changes_and_notify(watched_website_id: int):
    time.sleep(round(random.uniform(1, 10), 2))

    website = WatchedWebsite.objects.get(pk=watched_website_id)
    new_hash = get_website_hash(website.website_url)

    if new_hash != website.website_hash:
        bot.send_message(
            website.chat_id,
            "The website `{}` has changed".format(website.website_url),
        )

        website.website_hash = new_hash
        website.save()


@shared_task
def notify_about_changes():
    jobs = group(
        check_website_changes_and_notify.s(watched_website.id)
        for watched_website in WatchedWebsite.objects.all()
    )
    jobs.apply_async()

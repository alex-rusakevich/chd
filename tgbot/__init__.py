import os.path as op

from django.conf import settings

TG_WEBHOOK_PATH = "api/tgbot/webhook/"
TG_WEBHOOK_URL = op.join(settings.HOST_NAME, TG_WEBHOOK_PATH)

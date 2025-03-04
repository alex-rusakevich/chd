import telebot
from django.core.exceptions import BadRequest
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from tgbot.bot import bot


@csrf_exempt
def get_message(request: HttpRequest):
    if request.headers.get("content-type") == "application/json":
        json_string = request.body.decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])

        return HttpResponse("")
    else:
        raise BadRequest()

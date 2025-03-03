from django.db import models


class WatchedWebsite(models.Model):
    chat_id = models.IntegerField()
    website_url = models.CharField(max_length=512)
    website_hash = models.CharField(max_length=64)

from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=30)
    youtube_id = models.CharField(max_length=15)

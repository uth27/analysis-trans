from __future__ import unicode_literals
from django.db import models


class Result(models.Model):
    sentiment = models.TextField(max_length=250)
    classification = models.CharField(max_length=10)

class Tweets(models.Model):
    created_date = models.CharField(max_length=20)
    tweet_text = models.TextField(max_length=250)
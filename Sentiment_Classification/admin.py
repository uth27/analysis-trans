from django.contrib import admin
from Sentiment_Classification.models import *


class ResultAdmin(admin.ModelAdmin):
    list_display = ['sentiment', 'classification']
    list_filter = ()
    search_fields = ['sentiment']
    list_per_page = 25

admin.site.register(Result, ResultAdmin)

class TweetsAdmin(admin.ModelAdmin):
    list_display = ['created_date', 'tweet_text']
    list_filter = ()
    search_fields = ['tweet_text']
    list_per_page = 25

admin.site.register(Tweets, TweetsAdmin)



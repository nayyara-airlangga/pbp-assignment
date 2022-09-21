from django.db import models

# Create your models here.
class MyWatchlistRating(models.IntegerChoices):
    BAD = 1
    NOT_GOOD = 2
    OK = 3
    GOOD = 4
    GREAT = 5


class MyWatchlist(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.IntegerField(choices=MyWatchlistRating.choices)
    release_date = models.DateField()
    review = models.TextField()

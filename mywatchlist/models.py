from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class MyWatchlist(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.FloatField(
        validators=[MaxValueValidator(5.0), MinValueValidator(0.0)]
    )
    release_date = models.DateField()
    review = models.TextField()

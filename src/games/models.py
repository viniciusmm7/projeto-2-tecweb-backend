from django.db import models


class Game(models.Model):
    rawgID = models.IntegerField()
    # slug = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    # rating = models.FloatField()
    # ratingQty = models.IntegerField()

    def __str__(self):
        return f'{self.id}. {self.title}'

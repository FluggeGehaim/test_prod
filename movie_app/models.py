from django.db import models
from django.urls import reverse


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.FloatField(null=True)
    year = models.IntegerField(null=True)
    budget = models.IntegerField(null=True)

    def get_url(self):
        return reverse('look_movie', args=[self.id])

    def __str__(self):
        return f'Фильм {self.name}, Рейтинг {self.rating}%, Год выпуска - {self.year}, Стоимость: {self.budget} USD'

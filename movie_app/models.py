from django.db import models
from django.urls import reverse
from pytils.translit import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'

    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('solo_movie_path', args=[self.slug])

    def __str__(self):
        return f'Фильм:{self.name} -   рейтинг {self.rating}/100,  год выпуска {self.year},  Бюджет {self.budget}'


class Director(models.Model):
    first_name = models.CharField(max_length=40, default='Не указано')
    last_name = models.CharField(max_length=40, default='Не указано')
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

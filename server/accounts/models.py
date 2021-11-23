import os
from movies.models import Genre
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.fields.related import ForeignKey, ManyToManyField


class PickMovie(models.Model):
    title = models.CharField(max_length=20)
    poster_path = models.CharField(max_length=200)
    genre_ids = models.ManyToManyField(Genre, related_name='pickmovie_genre', null=True)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.title
    
class User(AbstractUser):
    moviepicks = models.ManyToManyField(PickMovie, blank=True, null=True, related_name='user_pick')
    # moviepicks = models.ForeignKey(PickMovie, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.username



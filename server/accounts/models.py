from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class PickMovie(models.Model):
    title = models.CharField(max_length=20)
    poster_path = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
class User(AbstractUser):
    moviepicks = models.ManyToManyField(PickMovie)

    def __str__(self):
        return self.username



from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Movie(models.Model):

    title = models.CharField(max_length=50)
    popularity = models.FloatField()
    genre_ids = models.ManyToManyField(Genre, related_name='movie_genre')
    release_date = models.DateField()
    overview = models.TextField()
    poster_path = models.TextField()
    like_users =  models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_review', blank=True)
    title = models.CharField(max_length=500)
    rank = models.FloatField()

    def __str__(self):
        return self.title




class Actor(models.Model):
    actor_id = models.IntegerField()
    name = models.CharField(max_length=100)
    profile_path = models.TextField(null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_actor')


    def __str__(self):
        return self.name

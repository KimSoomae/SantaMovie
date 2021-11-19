from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField

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

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_review')
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

from django.contrib import admin
from .models import ChristmasMovie, Genre, Movie, Review

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(ChristmasMovie)

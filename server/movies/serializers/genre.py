from rest_framework import serializers
from ..models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'
    movie_genre = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = '__all__'




class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id','name',)
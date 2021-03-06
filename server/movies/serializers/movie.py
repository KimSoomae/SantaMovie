from rest_framework import serializers
from ..models import Actor, Movie, Genre, Review,ChristmasMovie, ChristmasReview

class MovieSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name',)
    genre_ids = GenreSerializer(many=True, read_only=True)

    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = '__all__'
    movie_review = ReviewSerializer(many=True, read_only=True)

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = '__all__'
    movie_actor = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name',)
    genre_ids = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('id','title', 'overview','popularity','genre_ids','poster_path')


class ChristmasMovieListSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name',)
    genre_ids = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = ChristmasMovie
        fields = ('id','title', 'overview','popularity','genre_ids','poster_path','actors')


class ChristmasMovieSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name',)
    genre_ids = GenreSerializer(many=True, read_only=True)

    class ChristmasReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = ChristmasReview
            fields = '__all__'
    christmasmovie_review = ChristmasReviewSerializer(many=True, read_only=True)

    class Meta:
        model = ChristmasMovie
        fields = '__all__'
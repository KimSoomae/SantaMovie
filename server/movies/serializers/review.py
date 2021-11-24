from rest_framework import serializers
from ..models import Review, Movie,ChristmasReview, ChristmasMovie

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title',)


class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

class ChristmasReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChristmasReview
        fields = ('id', 'title',)


class ChristmasReviewSerializer(serializers.ModelSerializer):
    class ChristmasMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = ChristmasMovie
            fields = '__all__'

    christmasmovie = ChristmasMovieSerializer(read_only=True)

    class Meta:
        model = ChristmasReview
        fields = '__all__'
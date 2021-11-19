from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import PickMovie


class MoviePickListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PickMovie
        fields = ('id', 'title','poster_path')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class MoviePickSerializer(serializers.ModelSerializer):
        class Meta:
            model = PickMovie
            fields = ('title', 'poster_path')

    moviepicks = MoviePickSerializer(many=True, read_only=True)

    class Meta: 
        model = get_user_model()
        fields = ('username', 'password', 'moviepicks')


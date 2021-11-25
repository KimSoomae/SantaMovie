from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import PickMovie


class MoviePickListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PickMovie
        fields = ('id', 'title','poster_path')

class MoviePickSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickMovie
        fields = ('id', 'title','poster_path')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class MoviePickSerializer(serializers.ModelSerializer):
        class Meta:
            model = PickMovie
            fields = '__all__'

    moviepicks = MoviePickSerializer(read_only=True, many=True, allow_null=True)
    class Meta: 
        model = get_user_model()
        fields = ('username', 'password', 'moviepicks', 'first_genre', 'second_genre')

    # def create(self, validated_data):
    #     return get_user_model(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.moviepicks = validated_data.get('moviepicks', instance.content)
    #     instance.save()
    #     return instance
    
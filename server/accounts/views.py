from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer, MoviePickListSerializer
from movies.serializers.movie import MovieSerializer
from rest_framework.permissions import AllowAny
from .models import PickMovie, User
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from django.contrib.auth import get_user_model
from collections import defaultdict
import json

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    if password != password_confirmation:
        return Response({'error' : '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def get_loginuser(request):
    print(request.user)
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_movie_pick(request):
    if request.method == 'GET':
        moviepicks = PickMovie.objects.all()
        print(moviepicks)
        serializer = MoviePickListSerializer(moviepicks, many=True)
        
        return Response(serializer.data)

@api_view(['POST'])
def save_movie(request, movie_id):
    mymovie = get_object_or_404(PickMovie, pk=movie_id)
    user = get_object_or_404(User, pk=request.user.id)
    user.moviepicks.add(mymovie)
    user.save()
    print(user.moviepicks)
    return Response()


@api_view(['POST'])
def save_user_genre(request):
    genre_dict = defaultdict(int)
    user = get_object_or_404(User, pk=request.user.id)
    for movie in user.moviepicks.all():
        for genre in movie.genre_ids.all():
            genre_dict[genre.name] += 1
    sorted_genre_dict = sorted(genre_dict.items(), reverse=True, key=lambda item:item[1])
    print(sorted_genre_dict)
    user.first_genre = sorted_genre_dict[0][0]
    user.second_genre = sorted_genre_dict[1][0]
    user.save()
    return Response()


@api_view(['GET'])
def get_recommend_movie(request):
    recommend_movie_list = []
    user = get_object_or_404(User, pk=request.user.id)
    print(user.username)
    users = User.objects.all()
    for check_user in users:
        if check_user == user: 
            continue
        if (check_user.first_genre == user.first_genre and check_user.second_genre == user.second_genre) or (check_user.first_genre == user.second_genre and check_user.second_genre == user.first_genre):
            recommend_movie = check_user.like_movies.all()
            for r_movie in recommend_movie:
                recommend_movie_list.append(r_movie)
        elif (check_user.first_genre == user.first_genre or check_user.second_genre == user.second_genre) or (check_user.first_genre == user.second_genre or check_user.second_genre == user.first_genre):
            recommend_movie = check_user.like_movies.all()
            for r_movie in recommend_movie:
                recommend_movie_list.append(r_movie)
        serializer = MovieSerializer(set(recommend_movie_list), many=True)
    return Response(serializer.data)
    
           

@api_view(['GET'])
def get_user(request,user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer, MoviePickListSerializer, MoviePickSerializer
from rest_framework.permissions import AllowAny
from .models import PickMovie, User
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from django.contrib.auth import get_user_model

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
    print(f'여기ㄷ까지 들어오니!!!!!{movie_id}')
    mymovie = get_object_or_404(PickMovie, pk=movie_id)
    user = get_object_or_404(User, pk=request.user.id)
    user.moviepicks.add(mymovie)
    user.save()
    print(user.moviepicks)
  

    return Response()
    #return Response(user)
    # print(mymovie)
    # movieserializer = MoviePickSerializer(mymovie)
    # #userserializer = UserSerializer(user, data=movieserializer)
    # print(f'유저는 {user}')
    # if request.method == 'POST':
    #      print(f'여기도 들어오니??')
    #      serializer = UserSerializer(data=user)
         
    #      print(serializer.data)

    #      if serializer.is_valid(raise_exception=True):
    #         print(f'여기도 들어오니??!!!!!!!')
    #         serializer.save(moviepicks = mymovie)
    #         return Response(serializer.data)
# @api_view(['POST'])
# def save_movie(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(request.user)
#         user.moviepicks += 


@api_view(['GET'])
def get_user(request,user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

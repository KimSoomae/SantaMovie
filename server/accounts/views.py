from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer, MoviePickListSerializer
from rest_framework.permissions import AllowAny
from .models import PickMovie
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status

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

@api_view(['GET'])
@permission_classes([AllowAny])
def get_movie_pick(request):
    if request.method == 'GET':
        moviepicks = PickMovie.objects.all()
        print(moviepicks)
        serializer = MoviePickListSerializer(moviepicks, many=True)
        return Response(serializer.data)

# @api_view(['POST'])
# def save_movie(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(request.user)
#         user.moviepicks += 
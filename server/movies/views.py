from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import  Movie, Review
from .serializers.movie import MovieSerializer, MovieListSerializer
from .serializers.review import ReviewSerializer, ReviewListSerializer
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == "GET":
        movies = get_list_or_404(Movie)
        serializers = MovieListSerializer(movies, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)



@api_view(['GET','POST'])
def movie_review_create(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        reviews = movie.movie_review.all()
        serializer = ReviewListSerializer(reviews,many=True)
        return Response(serializer.data)

    else:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def movie_review_update_delete(request,review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'PUT':
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        data = {
            'message':f'{review_pk}번째 리뷰가 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)
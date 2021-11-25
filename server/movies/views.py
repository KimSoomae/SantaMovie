from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import  Movie, Review, ChristmasMovie, ChristmasReview
from .serializers.movie import MovieSerializer, MovieListSerializer, ChristmasMovieSerializer, ChristmasMovieListSerializer
from .serializers.review import ReviewSerializer, ReviewListSerializer, ChristmasReviewListSerializer, ChristmasReviewSerializer
from rest_framework import status
from django.views.decorators.http import require_POST
from django.db.models import Count 


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == "GET":
        # movies = Movie.objects.all().order_by('')
        movies = Movie.objects.annotate(likes=Count('like_users')).all().order_by('-likes')
        serializers = MovieListSerializer(movies, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def christmasmovie_list(request):
    if request.method == "GET":
        christmasmovies = ChristmasMovie.objects.order_by('?')
        serializers = ChristmasMovieListSerializer(christmasmovies, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = ChristmasMovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def christmasmovie_detail(request, christmasmovie_pk):
    christmasmovie = get_object_or_404(ChristmasMovie, pk=christmasmovie_pk)
    serializer = ChristmasMovieSerializer(christmasmovie)
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
            serializer.save(movie=movie, user=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def movie_review_update_delete(request,review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if not request.user.review_set.filter(pk=review_pk).exists():
        return Response({'detail' : '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        print('여기까지 왔음><><><><')
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

@api_view(['GET','POST'])
def christmasmovie_review_create(request, christmasmovie_pk):
    if request.method == 'GET':
        christmasmovie = get_object_or_404(ChristmasMovie, pk=christmasmovie_pk)
        christmasreviews = christmasmovie.christmasmovie_review.all()
        serializer = ChristmasReviewListSerializer(christmasreviews,many=True)
        return Response(serializer.data)

    else:
        christmasmovie = get_object_or_404(ChristmasMovie, pk=christmasmovie_pk)
        serializer = ChristmasReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(christmasmovie=christmasmovie, user=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def christmasmovie_review_update_delete(request,christmasreview_pk):
    christmasreview = get_object_or_404(ChristmasReview, pk=christmasreview_pk)

    if not request.user.review_set.filter(pk=christmasreview_pk).exists():
        return Response({'detail' : '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = ChristmasReviewSerializer(instance=christmasreview, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        christmasreview.delete()
        data = {
            'message':f'{christmasreview_pk}번째 리뷰가 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def like(request, movie_pk):        
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user
        if request.method == 'GET':
            if movie.like_users.filter(pk=user.pk).exists():
                key = True
            else:
                key = False
            context = {
                'key' : key,
                'like_users': movie.like_users.count() 
            }
            return Response(context) 
        else:
            if movie.like_users.filter(pk=user.pk).exists():
                movie.like_users.remove(user)
                key = False
            else:
                movie.like_users.add(user)
                key = True
            context = {
                'key' : key,
                'like_users' : movie.like_users.count()            
                }
            return Response(context) 


@api_view(['POST', 'GET'])
def christmaslike(request, christmasmovie_pk):        
    if request.user.is_authenticated:
        movie = get_object_or_404(ChristmasMovie, pk=christmasmovie_pk)
        user = request.user
        if request.method == 'GET':
            if movie.like_users.filter(pk=user.pk).exists():
                key = True
            else:
                key = False
            context = {
                'key' : key,
                'like_users': movie.like_users.count() 
            }
            return Response(context) 
        else:
            if movie.like_users.filter(pk=user.pk).exists():
                movie.like_users.remove(user)
                key = False
            else:
                movie.like_users.add(user)
                key = True
            context = {
                'key' : key,
                'like_users' : movie.like_users.count()            
                }
            return Response(context) 

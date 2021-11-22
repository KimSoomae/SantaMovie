from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    #path('reviews/', views.review_list),
    path('movies/<int:movie_pk>/reviews/', views.movie_review_create),
    path('reviews/<int:review_pk>/', views.movie_review_update_delete),
    path('<int:movie_pk>/like/', views.like, name='like'),

]
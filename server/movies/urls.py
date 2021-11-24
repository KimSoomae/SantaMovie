from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    #path('reviews/', views.review_list),
    path('movies/<int:movie_pk>/reviews/', views.movie_review_create),
    path('reviews/<int:review_pk>/', views.movie_review_update_delete),
    path('<int:movie_pk>/like/', views.like, name='like'),
    path('christmasmovies/', views.christmasmovie_list),
    path('christmasmovies/<int:christmasmovie_pk>/', views.christmasmovie_detail),
    path('christmasmovies/<int:christmasmovie_pk>/christmasreviews/', views.christmasmovie_review_create),
    path('christmasreviews/<int:christmasreview_pk>/', views.christmasmovie_review_update_delete),

]
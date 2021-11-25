from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name="accounts"

urlpatterns = [
    path('get-pick-movie/', views.get_movie_pick),
    path('signup/', views.signup),
    path('save-movie/<int:movie_id>/', views.save_movie),
    path('api-token-auth/', obtain_jwt_token),
    path('get-user/', views.get_loginuser),
    path('getuser/<int:user_id>/', views.get_user),
    path('check_same_user/<int:user_id>/', views.check_same_user),
    path('save_user_genre/', views.save_user_genre),
    path('get_recommend_movie/', views.get_recommend_movie),
    path('get_like_movie/', views.get_like_movie)
]
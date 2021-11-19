from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name="accounts"

urlpatterns = [
    path('get-pick-movie/', views.get_movie_pick),
    path('signup/', views.signup),
    #path('save-movie/<int:movie_id>/', views.save_movie),
    path('api-token-auth/', obtain_jwt_token),
]
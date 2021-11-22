from django.urls import path, include
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

app_name = 'community'

urlpatterns = [
    path('', views.community_list_create),
    path('search/<search>/', views.community_search),
    path('api-token-auth/', obtain_jwt_token),
    path('<int:community_pk>/', views.community_update_delete),
    path('<int:community_pk>/comments/', views.comment_list_create),
    path('comment/<int:comment_pk>/', views.comment_update_delete),   
    
]
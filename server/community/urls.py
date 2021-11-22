from django.urls import path, include
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
app_name = 'community'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('api-token-auth/', obtain_jwt_token),
    path('api-jwt-auth/refresh/', refresh_jwt_token), # JWT 토큰 갱신
    path('api-jwt-auth/verify/$', verify_jwt_token),   # JWT 토큰 확인
    path('<int:community_pk>/', views.detail, name='detail'),
    path('delete/<int:community_pk>', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:community_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
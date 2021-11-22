from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'community'

urlpatterns = [
    
    path('', views.community_list_create),
    path('api-token-auth/', obtain_jwt_token),
    path('<int:community_pk>/', views.community_update_delete),
    path('<int:community_pk>/comments/', views.comment_list_create),
    path('comment/<int:comment_pk>/', views.comment_update_delete),
    # path('delete/<int:community_pk>', views.delete, name='delete'),
    # path('create/', views.create, name='create'),
    # path('<int:pk>/update', views.update, name='update'),
    # path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    # path('<int:community_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    
]
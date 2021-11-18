from rest_framework import serializers
from .models import Community, Comment, Tag
from .. import UserSerializer, User
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fileds = ('name')
        
class CommunitySerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True)
    tags = serializers.StringRelatedField(many=True)
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id','username')
    user = UserSerializer(read_only=True)

    class Meta:
        model = Community
        fields = ('id', 'title', 'content', 'user', 'comments', 'tags')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('title', 'created_at', 'updated_at', 'user',)
    
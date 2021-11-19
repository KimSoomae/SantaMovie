from rest_framework import serializers
from .models import Community, Comment, Tag
from django.conf import settings
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class CommunitySerializer(serializers.ModelSerializer):
    class TagSerializer(serializers.ModelSerializer):
        class Meta:
            model = Tag
            fields = '__all__'
    tags = TagSerializer(read_only=True)

    class Meta:
        model = Community
        fields = ('id', 'title', 'content', 'tags',)

class CommentSerializer(serializers.ModelSerializer):
    # class UserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = User
    #         fields = ('id','username')
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('title', 'created_at', 'updated_at',)
    
from django.db.models import fields
from rest_framework import serializers
from .models import Community, Comment, Tag
from django.conf import settings

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CommunityListSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()
    def get_userName(self,obj):
        return obj.user.username

    class Meta:
        model = Community
        fields = ('id', 'title','user','userName')


class CommunitySerializer(serializers.ModelSerializer):

    class TagSerializer(serializers.ModelSerializer):
        class Meta:
            model = Tag
            fields = '__all__'
    tags = TagSerializer(many=True, read_only=True)
    #tags_id = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), write_only=True,many=True)

    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'
    comments = CommentSerializer(many=True, read_only=True)
    userName = serializers.SerializerMethodField()
    def get_userName(self,obj):
         return obj.user.username
    class Meta:
        model = Community
        fields = ('id', 'title', 'content', 'tags', 'created_at','updated_at', 'comments', 'user', 'userName')



class CommentSerializer(serializers.ModelSerializer):
    class CommunitySerializer(serializers.ModelSerializer):
        class Meta:
            model = Community
            fields = '__all__'
    community = CommunitySerializer(read_only=True)
    userName = serializers.SerializerMethodField()
    def get_userName(self,obj):
         return obj.user.username
    class Meta:
        model = Comment
        fields = '__all__'
    
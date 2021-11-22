from django.db.models import fields
from rest_framework import serializers
from .models import Community, Comment, Tag
from django.conf import settings

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CommunityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('id', 'title','user')


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

    class Meta:
        model = Community
        fields = ('id', 'title', 'content', 'tags', 'created_at','updated_at', 'comments', 'user')

    # def get_validation_exclusions(self, *args, **kwargs):
    #     exclusions = super(CommunitySerializer, self).get_validation_exclusions()

    #     return exclusions + ['user']

    # def create(self, validated_data):
    #     tags = validated_data.pop('tags_id')
    #     communities = Community.objects.create(**validated_data)
    #     for tg in tags:
    #         communities.tags.add(tg)
    #     return communities


class CommentSerializer(serializers.ModelSerializer):
    # class UserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = User
    #         fields = ('id','username')
    # user = UserSerializer(read_only=True)
    class CommunitySerializer(serializers.ModelSerializer):
        class Meta:
            model = Community
            fields = '__all__'
    community = CommunitySerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
    
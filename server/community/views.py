from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Community, Comment
from .serializers import CommunityListSerializer, CommunitySerializer, CommentSerializer



@api_view(['GET', 'POST'])
def community_list_create(request):
    if request.method == 'GET':
        communitys = Community.objects.all()
        serializer = CommunityListSerializer(communitys, many=True)
        return Response(serializer.data)
    else:
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET','PUT', 'DELETE'])
def community_update_delete(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)

    if request.method == 'GET':
        serializer = CommunitySerializer(community)
        return Response(serializer.data)
    
    if not request.user.todo_set.filter(pk=community.pk).exists():
        return Response({'detail' : '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = CommunitySerializer(community, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        community.delete()
        return Response({ 'id': community_pk })


@api_view(['GET','POST'])
def comment_list_create(request, community_pk):
    if request.method == 'GET':
        community = get_object_or_404(Community, pk=community_pk)
        comments = community.comments.all()
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)

    else:
        community = get_object_or_404(Community, pk=community_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(community=community, user=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_delete(request,comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'detail' : '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'message':f'{comment_pk}번째 리뷰가 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)

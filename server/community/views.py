from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Community, Comment
from .forms import CommunityForm, CommentForm
from django.db.models import Count, Avg, Prefetch
# Create your views here.
@require_safe
def index(request):
    communities = Community.objects\
                .annotate(comment_count=Count('comment'))\
                .select_related('user')
    context = {
        'communities': communities,
    }
    return render(request, 'community/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = form.save(commit=False)
            community.user = request.user
            community.save()
            return redirect('community:detail', community.pk)
    else:
        form = CommunityForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_safe
def detail(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    comment_form = CommentForm()
    comments = community.comment_set.all()
    context = {
        'community': community,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


#@login_required

#@require_http_methods(['POST'])
@require_POST
def delete(request, community_pk):
    print(f'메소드!!!!!!!!!!!!!!{request.method}')
    community = get_object_or_404(Community, pk=community_pk)
    if request.user.is_authenticated:
        if request.user == community.user: 
            community.delete()
            return redirect('community:index')
    return redirect('community:detail', community.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    community = get_object_or_404(Community, pk=pk)
    if request.user == community.user:
        if request.method == 'POST':
            form = CommunityForm(request.POST, instance=community)
            if form.is_valid():
                form.save()
                return redirect('community:detail', community.pk)
        else:
            form = CommunityForm(instance=community)
    else:
        return redirect('community:index')
    context = {
        'community': community,
        'form': form,
    }
    return render(request, 'community/update.html', context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        community = get_object_or_404(Community, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.community = community
            comment.user = request.user
            comment.save()
        return redirect('community:detail', community.pk)
    # login 구현하기
    return redirect('accounts:login')


@require_POST
def comments_delete(request, community_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('community:detail', community_pk)


# @require_POST
# def likes(request, review_pk):
#     if request.user.is_authenticated:
#         review = get_object_or_404(Review, pk=review_pk)
#         if review.review_like.filter(pk=request.user.pk).exists():
#             review.review_like.remove(request.user)
#         else:
#             review.review_like.add(request.user)
#         return redirect('community:index')
#     return redirect('accounts:login')












# from django.shortcuts import get_object_or_404, render
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from .serializers import CommunitySerializer, CommentSerializer, TagSerializer
# from .models import Community, Comment, Tag
# from rest_framework.permissions import AllowAny
# from django.contrib.auth.decorators import login_required
# # Create your views here.

# @api_view(['GET', 'POST'])
# #@permission_classes([AllowAny])
# @login_required
# def community_create(request):
#     if request.method == 'GET':
#         communities = Community.objects.all()
#         serializer = CommunitySerializer(communities, many=True)
#         return Response(serializer.data)
#     # 게시글 작성
#     else:
#         serializer = CommunitySerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# def community_detail(request, community_pk):
#     community = get_object_or_404(Community, pk=community_pk)
#     if not request.user.todo_set.filter(pk=community_pk).exists():
#         return Response({'detail': '권한이 없습니다'}, status=status.HTTP_403_FORBIDDEN)
#     serializer = CommunitySerializer(community)
#     return Response(serializer.data)


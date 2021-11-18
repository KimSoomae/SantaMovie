from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CommunitySerializer, CommentSerializer, TagSerializer
from .models import Community, Comment, Tag
# Create your views here.

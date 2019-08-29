from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView

from news.models import File, News
from .serializers import DocumentSerializer


class News_Create(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = DocumentSerializer

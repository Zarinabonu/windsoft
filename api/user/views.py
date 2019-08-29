from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from .serializers import User_Serializer
from django.contrib.auth.models import User


class User_CreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = User_Serializer

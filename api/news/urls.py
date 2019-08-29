from django.contrib import admin
from django.urls import path, include

from api.news import views

urlpatterns = [
    path('create/', views.News_Create.as_view(), name='api-news-create'),

]
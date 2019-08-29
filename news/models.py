from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)


class File(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE)
    file = models.FileField(upload_to='file/')

# Create your models here.

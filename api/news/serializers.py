from django.contrib.auth.models import User

from news.models import News, File
from rest_framework.serializers import ModelSerializer


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'description',)

    def create(self, validated_data):
        news = News(**validated_data)
        request = self.context['request']
        user = User.objects.get(id=request.user.id)
        fi = News.objects.create(sender=user, title=news.title, description=news.description)
        files = request.data.getlist('file')
        for file in files:
            f = File.objects.create(news=fi, file=file)
            f.save()

        return fi
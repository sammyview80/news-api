from rest_framework import serializers

from .models import NewsModel


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = '__all__'

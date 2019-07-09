from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

from main.models.tag import Tag


class New(models.Model):
    """
    ID
    Title
    Text
    Images
    Tags
    """
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=1000)
    image = models.ImageField()
    tags = models.ManyToManyField(Tag, related_name="news")


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = "__all__"

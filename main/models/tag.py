from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers


class Tag(models.Model):
    """
    id
    name
    """
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ["name"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
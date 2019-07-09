from main.models.news import New, NewsSerializer
from main.models.tag import Tag

from rest_framework import viewsets


class NewsViewset(viewsets.ReadOnlyModelViewSet):
    model = New
    serializer_class = NewsSerializer

    def get_queryset(self):
        tags = self.request.GET.get("tags").split(",")

        if tags:
            return New.objects.filter(tags__name__in=obj_tags).distinct()
        else:
            return New.objects.all()

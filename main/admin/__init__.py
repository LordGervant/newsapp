from django.contrib import admin

from main.models.news import New
from main.models.tag import Tag


class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in New._meta.fields]

class TagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tag._meta.fields]

admin.site.register(New, NewsAdmin)
admin.site.register(Tag, TagAdmin)

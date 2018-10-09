from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'id',
        'author',
        'create_time',
        'update_time',
        'is_deleted'
    ]
    ordering = ['id']


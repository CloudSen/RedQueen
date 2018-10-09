from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=10)
    tag = models.CharField(max_length=10)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

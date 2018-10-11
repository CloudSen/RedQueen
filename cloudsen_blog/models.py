from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, default='Please input description')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, db_constraint=False, on_delete=models.DO_NOTHING)
    tag = models.ForeignKey(Tag, db_constraint=False, on_delete=models.DO_NOTHING)
    content = models.TextField()
    summary = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

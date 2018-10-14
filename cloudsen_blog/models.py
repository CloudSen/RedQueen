from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


# 文章标签类
class Tag(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, default='Please input description')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# 文章类
class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, db_constraint=False, on_delete=models.DO_NOTHING)
    tag = models.ForeignKey(Tag, db_constraint=False, on_delete=models.DO_NOTHING)
    content = MarkdownxField()
    summary = MarkdownxField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    @property
    def formatted_content(self):
        return markdownify(self.content)

    @property
    def formatted_summary(self):
        return markdownify(self.summary)

    def __str__(self):
        return self.title


# 说说类
class MyIdea(models.Model):
    author = models.ForeignKey(User, db_constraint=False, on_delete=models.DO_NOTHING)
    content = MarkdownxField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    def __str__(self):
        return self.content

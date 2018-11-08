from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Tag(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, default='Please input description')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def get_articles_count_with_same_tag(self):
        return self.article_set.count()

    def __str__(self):
        return self.name


class CardType(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, default='Please input description')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    COLOR_THEME = [
        ('text-muted', 'muted color'),
        ('text-light', 'white color '),
        ('text-dark', 'black color'),
        ('text-gray', 'gray color'),
    ]
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, db_constraint=False, on_delete=models.DO_NOTHING)
    tag = models.ForeignKey(Tag, db_constraint=False, on_delete=models.DO_NOTHING)
    card_type = models.ForeignKey(CardType, db_constraint=False, on_delete=models.DO_NOTHING)
    preview_pic_url = models.CharField(max_length=500, null=True, blank=True)
    text_color = models.CharField(max_length=30, choices=COLOR_THEME, default='gray color')
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


class SiteTimeLine(models.Model):
    title = models.CharField(max_length=30)
    content = MarkdownxField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    title = models.CharField(max_length=30)
    content = MarkdownxField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    def __str__(self):
        return self.title


class FriendsLink(models.Model):
    name = models.CharField(max_length=30)
    introduce = MarkdownxField()
    site_url = models.CharField(max_length=300)
    avatar_url = models.CharField(max_length=300)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    @property
    def formatted_markdown(self):
        return markdownify(self.introduce)

    def __str__(self):
        return self.name

from django.shortcuts import render
from django.http import HttpRequest
import cloudsen_blog.models as models


def go_home_page(request: HttpRequest):
    """redirect to home page"""
    return render(request, 'cloudsen_blog/cloudsen-index.html')


def go_blog_page(request: HttpRequest):
    """redirect to blog page"""
    articles = list_all_articles()
    context = {'articles': articles}
    return render(request, 'cloudsen_blog/blog.html', context)


def go_article_detail_page(request: HttpRequest, article_pk: int):
    """redirect to article's detail page"""
    article = models.Article.objects.get(pk=article_pk)
    context = {'article': article}
    return render(request, 'cloudsen_blog/article-detail.html', context)


def go_same_tag_articles_page(request: HttpRequest, tag_name: str):
    """redirect to page that shows all articles with same tag"""
    pass


def list_all_articles():
    """get a list of all my articles"""
    return models.Article.objects.all()


def get_article_detail(article_pk: int):
    """retuen an article's detail, searching by primary key"""
    pass


def list_same_tag_articles(tag_name: str):
    """return a list of articles with same tag"""
    pass

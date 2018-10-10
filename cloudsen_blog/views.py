from django.shortcuts import render
from django.http import HttpRequest


def go_home(request: HttpRequest):
    return render(request, 'cloudsen-index.html')


def list_all_articles(request: HttpRequest):
    pass


def show_article_detail(request: HttpRequest, article_pk: int):
    pass


def show_same_tag_article(request: HttpRequest, article_tag: str):
    pass

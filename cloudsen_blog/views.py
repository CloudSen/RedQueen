from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator
from django.utils import timezone
import cloudsen_blog.models as models


def go_home_page(request: HttpRequest):
    """redirect to home page"""
    return render(request, 'cloudsen_blog/home/cloudsen-index.html')


def go_blog_page(request: HttpRequest):
    """redirect to blog page"""
    page_num = request.GET.get('page_num', 1)
    page, page_range = page_latest_2_month_articles(page_num)
    context = {
        'page_range': page_range,
        'page': page,
        'tags': list_all_tags(),
        'ideas': list_all_my_idea()}
    return render(request, 'cloudsen_blog/blog/blog.html', context)


def go_article_detail_page(request: HttpRequest, article_pk: int):
    """redirect to article's detail page"""
    article = get_article_detail(article_pk)
    context = {'article': article}
    return render(request, 'cloudsen_blog/blog/article-detail.html', context)


def go_tag_page(request: HttpRequest):
    """redirect to article tag page"""
    pass


def go_same_tag_articles_page(request: HttpRequest, tag_name: str):
    """redirect to page that shows all articles with same tag"""
    pass


def list_all_articles():
    """get a list of all my articles"""
    return models.Article.objects.all()


def page_latest_2_month_articles(page_number: int = 1):
    """
    paginate the articles published within two month

    :param page_number: expect page number
    :return: page and range
    """
    latest_2_month_date = timezone.now() - timezone.timedelta(days=60)
    latest_articles = models.Article.objects.filter(update_time__gte=latest_2_month_date).order_by('-update_time')
    return paginate_data(latest_articles, 10, page_number)


def get_article_detail(article_pk: int):
    """retuen an article's detail, searching by primary key"""
    return models.Article.objects.get(pk=article_pk)


def list_same_tag_articles(tag_name: str):
    """return a list of articles with same tag"""
    pass


def list_all_tags():
    return models.Tag.objects.all()


def list_all_my_idea():
    return models.MyIdea.objects.all()


def paginate_data(source_data, per_page: int, page_number: int):
    """
    only display two pages numbers before and after current page number

    :param source_data: object list
    :param per_page: how many data per page
    :param page_number: current page number
    :return: a tuple of page object and processed range
    """
    paginator = Paginator(source_data, per_page)
    page = paginator.get_page(page_number)
    page_range = [x for x in range(page.number - 2, page.number + 3) if 0 < x <= page.paginator.num_pages]
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if page.paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != page.paginator.num_pages:
        page_range.append(page.paginator.num_pages)
    return page, page_range

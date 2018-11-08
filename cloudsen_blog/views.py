from django.shortcuts import render, get_object_or_404, get_list_or_404
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
    page, page_range = paginate_latest_2_month_articles(page_num)
    context = {
        'page_range': page_range,
        'page': page,
        'tags': list_all_tags(),
        'ideas': list_all_my_idea(),
        'friends_link': list_friends_link(),
    }
    return render(request, 'cloudsen_blog/blog/blog.html', context)


def go_article_detail_page(request: HttpRequest, article_pk: int):
    """redirect to article's detail page"""
    article = get_article_detail(article_pk)
    context = {
        'article': article,
        'previous_article': models.Article.objects.filter(create_time__lt=article.create_time).last(),
        'next_article': models.Article.objects.filter(create_time__gt=article.create_time).first(),
    }
    return render(request, 'cloudsen_blog/blog/article-detail.html', context)


def go_tag_page(request: HttpRequest):
    """redirect to article tag page"""
    pass


def go_same_tag_articles_page(request: HttpRequest, tag_pk: int):
    """redirect to page that shows all articles with same tag"""
    tag = get_object_or_404(models.Tag, pk=tag_pk)
    page_num = request.GET.get('page_num', 1)
    page, page_range = paginate_same_tag_articles(tag_pk, page_num)
    context = {
        'page_range': page_range,
        'page': page,
        'tag': tag,
    }
    return render(request, 'cloudsen_blog/blog/same-tag-articles.html', context)


def go_site_timeline_page(request: HttpRequest):
    timelines = list_all_site_timeline()
    context = {'timelines': timelines}
    return render(request, 'cloudsen_blog/timeline/site-timeline.html', context)


def go_about_me_page(request: HttpRequest):
    about_me = get_about_me()
    context = {'about_me': about_me}
    return render(request, 'cloudsen_blog/about-me/about-me.html', context)


def go_monero_mine(request: HttpRequest):
    context = {}
    return render(request, 'cloudsen_blog/monero/monero.html', context)


def list_all_articles():
    """get a list of all my articles"""
    return models.Article.objects.filter(is_deleted=False)


def paginate_latest_2_month_articles(page_number: int = 1):
    """
    paginate the articles published within two month

    :param page_number: expect page number
    :return: page and range
    """
    latest_2_month_date = timezone.now() - timezone.timedelta(days=60)
    latest_articles = models.Article.objects.filter(update_time__gte=latest_2_month_date, is_deleted=False) \
        .order_by('-update_time')
    return paginate_data(latest_articles, 10, page_number)


def get_article_detail(article_pk: int):
    """retuen an article's detail, searching by primary key"""
    return get_object_or_404(models.Article, pk=article_pk, is_deleted=False)


def paginate_same_tag_articles(tag_pk: int, page_number: int = 1):
    """return a list of articles with same tag"""
    articles = get_list_or_404(models.Article, tag_id=tag_pk, is_deleted=False)
    return paginate_data(articles, 10, page_number)


def list_all_tags():
    return models.Tag.objects.filter(is_deleted=False)


def list_all_my_idea():
    return models.MyIdea.objects.filter(is_deleted=False)


def list_all_site_timeline():
    return models.SiteTimeLine.objects.filter(is_deleted=False).order_by('create_time')


def get_about_me():
    return models.AboutMe.objects.filter(is_deleted=False).first()


def list_friends_link():
    return models.FriendsLink.objects.filter(is_deleted=False)


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

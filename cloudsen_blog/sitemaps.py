from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from cloudsen_blog.models import Article


class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = 'https'

    def items(self):
        return Article.objects.filter(is_deleted=False)

    @staticmethod
    def lastmod(obj):
        return obj.update_time


class StaticPageSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return ['go_cloudsen_home', 'go_blog_page', 'go_site_timeline', 'go_about_me', 'go_monero_mine']

    def location(self, obj):
        return reverse(obj)

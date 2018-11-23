from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from cloudsen_blog.sitemaps import ArticleSitemap, StaticPageSitemap

sitemap_info = {
    'sitemaps': {
        'articles': ArticleSitemap,
        'static_pages': StaticPageSitemap,
    },
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cloudsen_home/', include('cloudsen_blog.urls')),
    re_path(r'^markdownx/', include('markdownx.urls')),
    re_path(r'^sitemap\.xml$', sitemap, sitemap_info, name='sitemaps'),
]

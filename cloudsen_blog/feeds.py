from django.urls import reverse
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils.feedgenerator import Atom1Feed
from cloudsen_blog.models import Article


class ExtendedRSSFeed(Rss201rev2Feed):
    mime_type = 'application/xml'


class RssSiteNewsFeed(Feed):
    feed_type = ExtendedRSSFeed
    author_name = 'CloudSen'
    title = 'CloudSen\'s Blog | Less Is More.'
    link = 'https://www.yangyunsen.com'
    description = 'Less Is More. Don\'t Panic!'
    feed_url = 'https://www.yangyunsen.com/cloudsen_home/rss.xml'

    @staticmethod
    def items():
        # 获取所有未删除的文章，以创建时间倒叙
        return Article.objects.filter(is_deleted=False).order_by('-create_time')

    def item_title(self, item):
        # 文章标题
        return item.title

    def item_description(self, item):
        # 文章的概要
        return item.formatted_summary

    def item_link(self, item):
        # 文章的链接地址
        return reverse('go_article_detail', args=[item.id])

    def item_pubdate(self, item):
        # 文章创建时间
        return item.create_time

    def item_guid(self, item):
        # 返回空即可，要不然文章链接就要重复两边
        return


class AtomSiteNewsFeed(RssSiteNewsFeed):
    # ATOM功能，大致和RSS一样，只不过是两种订阅方式
    feed_type = Atom1Feed
    subtitle = RssSiteNewsFeed.description

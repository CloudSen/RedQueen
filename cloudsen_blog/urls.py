from django.urls import path, re_path
from cloudsen_blog import views
from cloudsen_blog.feeds import RssSiteNewsFeed, AtomSiteNewsFeed

urlpatterns = [
    # home page route
    path('', views.go_home_page, name='go_cloudsen_home'),

    # blog page route
    path('blog/', views.go_blog_page, name='go_blog_page'),
    # blog articles route
    path('blog/article/<int:article_pk>', views.go_article_detail_page, name='go_article_detail'),
    # blog artricles with same tag page route
    path('blog/tag/<str:tag_pk>/articles/', views.go_same_tag_articles_page, name='go_same_tag_articles'),
    # web site timeline route
    path('timeline/site-timeline/', views.go_site_timeline_page, name='go_site_timeline'),
    # about me page route
    path('about-me/', views.go_about_me_page, name='go_about_me'),
    # friends route
    path('friends/', views.go_friends_page, name='go_friends_page'),
    # miner page route
    path('monero-mine/', views.go_monero_mine, name='go_monero_mine'),
    # miner taken verification
    path('captcha-mine/taken-verification', views.captcha_mine_taken_verification,
         name='captcha_mine_taken_verification'),
    # RSS
    re_path(r'^rss\.xml$', RssSiteNewsFeed(), name='rss'),
    # Atom
    re_path(r'^atom\.xml$', AtomSiteNewsFeed(), name='atom'),
]

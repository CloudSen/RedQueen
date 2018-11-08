from django.urls import path
from . import views

urlpatterns = [
    # home page route
    path('', views.go_home_page, name='go_cloudsen_home'),

    # blog page route
    path('blog/', views.go_blog_page, name='go_blog_page'),
    # blog articles route
    path('blog/article/<int:article_pk>', views.go_article_detail_page, name='go_article_detail'),
    # blog tags page route
    path('blog/tag/<str:tag_pk>/articles/', views.go_same_tag_articles_page, name='go_same_tag_articles'),
    # site timeline route
    path('timeline/site-timeline', views.go_site_timeline_page, name='go_site_timeline'),
]

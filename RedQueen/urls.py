from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cloudsen_blog/', include('cloudsen_blog.urls')),
    re_path(r'^markdownx/', include('markdownx.urls'))
]

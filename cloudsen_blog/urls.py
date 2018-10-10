from django.urls import path
from . import views

urlpatterns = [
    path('', views.go_home, name='cloudsen_home')
]
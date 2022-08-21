from django.urls import path

from . import views

urlpatterns = [
    path('', views.detail, name='detail'),
    path('post', views.post, name='post'),
]
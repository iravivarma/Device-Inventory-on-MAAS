from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^insert/', views.insert, name='insert'),
    url(r'^update/', views.update, name='update'),
    url(r'^delete/', views.delete, name='delete'),
    url(r'^callback$', views.callback, name='callback'),
    url(r'^search$', views.search, name='search'),
]

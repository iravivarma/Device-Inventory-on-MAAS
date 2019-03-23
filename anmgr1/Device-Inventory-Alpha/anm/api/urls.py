from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^imprt/', views.imprt, name='imprt'),
    url(r'^export$', views.export, name='export')
]

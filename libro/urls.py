from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^libro/new/$', views.libro_new, name='libro_new'),
]

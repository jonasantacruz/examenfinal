from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('libro.urls')),
    #url(r'^libro/new/$', views.libro_new, name='libro_new'),
]

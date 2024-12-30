'''
App Folder URLs
'''
from django.contrib import admin
from django.urls import path
from Home import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 

handler404 = 'Home.views.NotFound404'
handler500 = 'Home.views.InternalError500'

urlpatterns = [
    path('', views.index, name="home"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
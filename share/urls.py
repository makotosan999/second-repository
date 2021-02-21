from django.contrib import admin
from django.urls import include, path
from . import views
from django.views.generic import base
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('mypage', views.mypage, name='mypage'),
    path('create', views.create, name='create'),
    path('edit/<int:num>',views.edit,name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('upload/', views.upload, name='upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) ##こっちたぶんいらない


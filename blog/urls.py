from django.urls import path,re_path, include
from . import views


urlpatterns = [
    path('', views.homepage_views, name='homepage'),
    path('<str:slug>-<id>', views.post_views, name='post'),
    path('category/<str:slug>', views.category_views, name="category")
]
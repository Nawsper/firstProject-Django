from django.urls import path
from AppBlog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('categoria/<int:categoria_id>/',
         views.categoria, name='categoria'),

]

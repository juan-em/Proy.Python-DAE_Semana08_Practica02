from django.urls import path

from . import views

app_name = 'Blog'

urlpatterns =[
    path('', views.index, name='index'),
    path('categoria/<int:categoria_id>', views.cat_post, name='cat_post')
]
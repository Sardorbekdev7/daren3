from django.urls import path
from .views import article_list, article_detail, article_archive


app_name = 'article'

urlpatterns = [
    path('', article_list, name='list'),
    path('list/', article_archive, name='archive'),
    path('detail/<slug:slug>', article_detail, name='detail')
]






from django.urls import path
from .views import *

urlpatterns = [
    path('news/', NewsList.as_view(), name='news'),
    path('news/<int:pk>', News_oneDetail.as_view(), name='post'),
    path('article/', ArticleList.as_view(), name='article'),
    path('article/<int:pk>', News_oneDetail.as_view()),
    path('category/', CategoryList.as_view(), name = 'category'),
    path('category_create/', CategoryCreate.as_view()),
    path('category/<int:pk>', CategoryUpdate.as_view()),
    path('news/create/', NewsCreate.as_view()),
    path('article/create/', ArticleCreate.as_view()),
    path('news/<int:pk>/update/', NewsUpdate.as_view()),
    path('article/<int:pk>/update/', ArticleUpdate.as_view()),
    path('news/<int:pk>/delete/', NewsDelete.as_view()),
    path('aticle/<int:pk>/delete/', ArticleDelete.as_view()),
    path('news/search/', NewsSearchList.as_view())
]
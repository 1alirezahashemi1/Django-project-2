from django.urls import path
from . views import  (
                        blog_detail,
                        category,
                        home ,
                        category ,
                        ArticlePreView,
                        )

# Write Your urls Here
app_name = 'blog'

urlpatterns = [
    path('',home,name='home'),
    path('page/<int:page>',home,name='home'),
    path('category/<slug:slug>/page/<int:page>',home,name='category_paginator'),
    path('blog/<slug:slug>',blog_detail,name='detail'),
    path('category/<slug:slug>',category,name='category'),
    path('Preview/<int:pk>',ArticlePreView.as_view(),name='article-preview')

]
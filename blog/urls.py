from django.urls import path
from . views import blog_detail, home 
# Write Your urls Here
app_name = 'blog'

urlpatterns = [
    path('',home,name='home'),
    path('blog/<slug:slug>',blog_detail,name='detail'),

]
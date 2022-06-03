from django.views.generic import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import Blog
# Create your views here.

# @login_required
# def Home(request):
#     return render(request,'registration/Home.html')

class ArticleList(ListView):
    template_name = 'registration/Home.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Blog.objects.all()
        else:
            return Blog.objects.filter(author = self.request.user)


   

    
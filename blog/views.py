from django.shortcuts import render
from . models import Blog
# Create your views here.
def home(request):
    context = {
        'blogs': Blog.objects.filter(status = "p")
    }
    return render(request,'index.html',context)


def blog_detail(request , slug):
    context = {
        'blog': Blog.objects.get (slug = slug)
    }
    return render(request,'post.html',context)
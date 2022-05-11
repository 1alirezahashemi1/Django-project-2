from django.shortcuts import render
from . models import Blog , Category

# Create your views here.

def home(request):
    context = {
        'blogs': Blog.objects.filter(status = "p"),  
    }
    return render(request,'index.html',context)

def blog_detail(request , slug):
    context = {
        'blog': Blog.objects.get (slug = slug),  
    }
    return render(request,'post.html',context)

def category(request,slug):
    category = Category.objects.get(slug = slug)
    context = {
        'category':category
    }
    return render(request, 'category.html',context)
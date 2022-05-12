from django.shortcuts import render
from . models import Blog , Category
from django.core.paginator import Paginator

# Create your views here.

def home(request,page=1):
    blog_list = Blog.objects.filter(status="p").order_by('-created')
    paginator = Paginator(blog_list, 3)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    context = {
        'blogs':  blogs
    }
    return render(request,'index.html',context)

def blog_detail(request , slug):
    context = {
        'blog': Blog.objects.get (slug = slug),  
    }
    return render(request,'post.html',context)

def category(request,slug , page=1):
    category = Category.objects.get(slug = slug)
    blogs = category.blogs.all()
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    blog_list = paginator.get_page(page_number)
  
    context = {
        'category':category ,
        'blogs':blog_list
    }
    return render(request, 'category.html',context)
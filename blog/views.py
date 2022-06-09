from django.shortcuts import get_object_or_404, render
from . models import Blog , Category
from django.core.paginator import Paginator
from django.views.generic import DetailView
from account.mixins import AuthorAccessMixin
# Create your views here.

def home(request,page=1):
    blog_list = Blog.objects.filter(status="p").order_by('-created')
    paginator = Paginator(blog_list, 3)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    context = {
        'blogs':  blogs
    }
    return render(request,'templates/Base/index.html',context)

def blog_detail(request , slug):
    context = {
        'blog': Blog.objects.get (slug = slug),  
    }
    return render(request,'templates/Base/post.html',context)

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
    return render(request, 'templates/Base/category.html',context)

class ArticlePreView(AuthorAccessMixin,DetailView):
    context_object_name = 'blogs'
    template_name = 'Base/index.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        return (Blog.objects.filter(pk=pk))
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Blog
from .mixins import *
# Create your views here.
class ArticleList(LoginRequiredMixin,ListView):
    template_name = 'registration/Home.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Blog.objects.all()
        else:
            return Blog.objects.filter(author = self.request.user)


class ArticleCreate(FieldMixin,FormValidMixin,LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'registration/create-update.html'


class ArticleUpdate(AuthorAccessMixin,FieldMixin,FormValidMixin,LoginRequiredMixin,UpdateView):
    model = Blog
    template_name = 'registration/create-update.html'
    

   

    
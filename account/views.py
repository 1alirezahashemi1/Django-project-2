from django.views.generic import *
from django.urls import reverse_lazy
from .models import User
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


class ArticleUpdate(AuthorAccessMixin,FieldMixin,FormValidMixin,UpdateView):
    model = Blog
    template_name = 'registration/create-update.html'
    

class ArticleDelete(SuperUserMixin,LoginRequiredMixin,DeleteView):
    model = Blog
    template_name = 'registration/blog_confirm_delete.html'
    success_url = reverse_lazy('account:home')

   

class Profile(UpdateView):
    model = User
    template_name = 'registration/profile.html' 
    fields = ['username','first_name','last_name','email','special_user','is_author']
    
    success_url = reverse_lazy('account:profile')
    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)
from django.views.generic import *
from django.urls import reverse_lazy
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Blog
from .mixins import *
from django.contrib.auth.views import LoginView
from .forms import ProfileForms
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

   

class Profile(LoginRequiredMixin,UpdateView):
    model = User
    template_name = 'registration/profile.html'
    form_class = ProfileForms 
    success_url = reverse_lazy('account:profile')
    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile,self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class Login(LoginView):
    def get_success_url(self):
        user = self.request.user

        if user.is_superuser or user.is_author:
            return reverse_lazy('account:home')
        else:
            return reverse_lazy('account:profile')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import Blog
# Create your views here.

@login_required
def Home(request):
    return render(request,'registration/Home.html')


    
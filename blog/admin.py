from django.contrib import admin
from . models import Blog
# Register your models here.

# First Model
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','slug','created','status']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status','title')
    search_fields = ('title','content')
    ordering = ('-created',)
    
admin.site.register(Blog,BlogAdmin)
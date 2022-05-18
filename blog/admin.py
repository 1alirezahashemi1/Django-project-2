from django.contrib import admin
from . models import Blog , Category
# Register your models here.

admin.site.site_header = 'وبلاگ جنگویی'
# First Model
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','slug','jcreated','category_to_str','status']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status','title')
    search_fields = ('title','content')
    ordering = ('-created',)

    def category_to_str(self,obj):
        return " , ".join([ str(item)  for item in obj.category.all()])
    category_to_str.short_description = 'دسته بندی'
    
admin.site.register(Blog,BlogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug','position','parent','status']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('title','status')
    search_fields = ('title',)

admin.site.register(Category,CategoryAdmin)
    
from django.db import models
from account.models import User
from django.urls import reverse
from extensions.utils import jalali_converter

# Create your models here
class Blog(models.Model):
    STATUS_CHOICES = (
        ('d',"draft"),
        ('p', "published"),
        ('i',"investigation"),
        ('b',"back"),
    )
    title = models.CharField(max_length=40,verbose_name="عنوان")
    slug = models.SlugField(verbose_name="ادرس مقاله")
    content = models.TextField(verbose_name='محتویات') 
    category = models.ManyToManyField("Category",verbose_name="دسته بندی ها",related_name='blogs')
    created = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name="تاریخ ساخت")
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    thumbnail = models.ImageField(upload_to = 'images/',verbose_name="عکس")
    status =  models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name="وضعیت مقاله")
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def get_absolute_url(self):
        return reverse('account:home')

    
    def __str__(self):
        return self.title

    def jcreated(self):
        return jalali_converter(self.created)
    jcreated.short_description = "تاریخ نوشتن"

class Category(models.Model):
    parent = models.ForeignKey('self',default=None,on_delete=models.SET_NULL,null=True,blank=True,related_name='children',verbose_name="زیر دسته")
    title = models.CharField(max_length=30,verbose_name="عنوان")
    slug = models.SlugField(verbose_name="ادرس")
    status = models.BooleanField(verbose_name="نشان داده شود ؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['parent__id',"position"] 

    def __str__(self):
        return self.title





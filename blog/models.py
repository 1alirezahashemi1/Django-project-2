from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    STATUS_CHOICES = (
        ('d',"draft"),
        ('p', "published")
    )
    title = models.CharField(max_length=40,verbose_name="عنوان")
    slug = models.SlugField(verbose_name="ادرس مقاله")
    content = models.TextField() 
    created = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name="تاریخ ساخت")
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    thumbnail = models.ImageField(upload_to = 'images/',verbose_name="عکس")
    status =  models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name="وضعیت مقاله")

    def __str__(self):
        return self.title


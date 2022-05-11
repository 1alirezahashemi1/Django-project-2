from django import template
from django.shortcuts import get_object_or_404
from ..models import Category
register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ جنگویی"

@register.inclusion_tag('template_tags/category-navbar.html')
def category_navbar():
    categories = Category.objects.filter(status =True)
    return {
        'categories': categories
    }
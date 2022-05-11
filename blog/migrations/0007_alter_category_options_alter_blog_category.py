# Generated by Django 4.0.1 on 2022-05-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_category_blog_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['position'], 'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(related_name='blogs', to='blog.Category', verbose_name='دسته بندی ها'),
        ),
    ]

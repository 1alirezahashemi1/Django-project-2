# Generated by Django 4.0.1 on 2022-06-09 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('d', 'draft'), ('p', 'published'), ('i', 'investigation'), ('b', 'back')], max_length=1, verbose_name='وضعیت مقاله'),
        ),
    ]

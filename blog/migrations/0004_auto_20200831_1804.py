# Generated by Django 3.1 on 2020-08-31 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

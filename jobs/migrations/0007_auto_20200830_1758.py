# Generated by Django 3.1 on 2020-08-30 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_job_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]

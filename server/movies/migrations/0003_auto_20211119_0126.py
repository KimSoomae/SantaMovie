# Generated by Django 3.2.6 on 2021-11-19 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20211118_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='content',
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]

# Generated by Django 3.2.6 on 2021-11-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_alter_community_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
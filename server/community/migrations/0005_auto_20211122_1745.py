# Generated by Django 3.2.6 on 2021-11-22 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0004_auto_20211122_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='tags',
            field=models.ManyToManyField(related_name='communities', to='community.Tag'),
        ),
        migrations.AlterField(
            model_name='community',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

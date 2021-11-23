# Generated by Django 3.2.6 on 2021-11-23 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_pickmovie_genre_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='moviepicks',
        ),
        migrations.AddField(
            model_name='user',
            name='moviepicks',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_pick', to='accounts.PickMovie'),
        ),
    ]
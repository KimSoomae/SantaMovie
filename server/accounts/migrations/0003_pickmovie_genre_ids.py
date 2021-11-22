# Generated by Django 3.2.6 on 2021-11-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_actor_profile_path'),
        ('accounts', '0002_alter_user_moviepicks'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickmovie',
            name='genre_ids',
            field=models.ManyToManyField(null=True, related_name='pickmovie_genre', to='movies.Genre'),
        ),
    ]
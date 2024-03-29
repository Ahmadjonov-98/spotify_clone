# Generated by Django 5.0.3 on 2024-03-15 14:25

import apps.user.managers
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0003_remove_album_songs_song_album_alter_artist_id"),
        ("user", "0002_user_followings"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("manager", apps.user.managers.UserManager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="artist_following",
            field=models.ManyToManyField(related_name="users", to="music.artist"),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="birthdate",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="country",
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="gender",
            field=models.CharField(
                choices=[("M", "male"), ("F", "female")], max_length=6, null=True
            ),
        ),
    ]

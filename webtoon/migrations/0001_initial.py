# Generated by Django 4.1.3 on 2022-12-06 06:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Webtoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=30)),
                ('image_url', models.CharField(max_length=60)),
                ('summary', models.TextField()),
                ('genre', models.CharField(max_length=20)),
                ('day_of_the_week', models.CharField(max_length=10)),
                ('webtoon_link', models.CharField(max_length=100)),
                ('webtoon_bookmarks', models.ManyToManyField(related_name='user_bookmarks', to=settings.AUTH_USER_MODEL)),
                ('webtoon_likes', models.ManyToManyField(related_name='user_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

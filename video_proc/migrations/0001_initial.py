# Generated by Django 3.0.3 on 2020-10-31 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=50)),
                ('text', models.CharField(blank=True, max_length=2000)),
                ('video_ref', models.CharField(blank=True, max_length=2000)),
                ('exp', models.IntegerField(default=100)),
                ('slug', models.SlugField(default='123', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionRecording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('video', models.FileField(blank=True, upload_to='user_videos')),
                ('trajectory', models.TextField(default='')),
                ('recognition', models.FileField(blank=True, upload_to='user_videos_recogned')),
                ('recognized', models.BooleanField(default=False)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video_proc.Competition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
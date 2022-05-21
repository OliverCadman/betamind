# Generated by Django 4.0.4 on 2022-05-21 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('create_post', models.DateTimeField(auto_now_add=True)),
                ('edit_post', models.DateTimeField(auto_now_add=True)),
                ('delete_post', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'ordering': ['-create_post'],
            },
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('mood', models.CharField(choices=[('Happy', 'Happy'), ('Sad', 'Sad'), ('Angry', 'Angry'), ('Surprised', 'Surprised'), ('Scared', 'Scared'), ('Disgusted', 'Disgusted'), ('Anxious', 'Anxious'), ('Bored', 'Bored'), ('Tired', 'Tired'), ('Depressed', 'Depressed'), ('Frustrated', 'Frustrated')], default='Happy', max_length=254)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Mood',
                'verbose_name_plural': 'Moods',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254, unique=True)),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_public', models.BooleanField(default=False)),
                ('mood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.mood')),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'ordering': ['-created_at'],
            },
        ),
    ]
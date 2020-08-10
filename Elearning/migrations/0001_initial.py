# Generated by Django 2.1.7 on 2020-08-10 08:26

import Elearning.models
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
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cid', models.IntegerField(null=True)),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Classroom',
                'ordering': ['cid'],
            },
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('your_file', models.FileField(upload_to=Elearning.models.Homework.path_and_rename)),
                ('description', models.TextField(blank=True, null=True)),
                ('added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning.Classroom')),
            ],
            options={
                'verbose_name_plural': 'Homeworks',
                'ordering': ['-added'],
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique_for_date='publish')),
                ('video_detail', models.TextField(blank=True, null=True)),
                ('video', models.CharField(max_length=300)),
                ('publish', models.DateField(default=django.utils.timezone.now)),
                ('created', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning.Classroom')),
                ('homework', models.ManyToManyField(blank=True, to='Elearning.Homework')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('profile_picture', models.ImageField(null=True, upload_to='images/profile_picture/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('profile_picture', models.ImageField(null=True, upload_to='images/profile_picture/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lecture',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning.Subject'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='subject',
            field=models.ManyToManyField(to='Elearning.Subject'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

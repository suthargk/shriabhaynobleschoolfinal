# Generated by Django 2.1.7 on 2019-05-07 08:15

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=200)),
                ('cover_photo', models.ImageField(upload_to='images/')),
                ('event_date', models.DateField()),
                ('event_venue', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Achievements',
            },
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('your_file', models.FileField(upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Faculty',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
                ('cover_photo', models.ImageField(null=True, upload_to='images/')),
                ('event_date', models.DateField()),
                ('last_update', models.DateField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Nobles.Gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Infrastructure_and_Facilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Infrastructure and Facilities',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350)),
                ('last_updated', models.DateField(auto_now=True)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
            ],
            options={
                'verbose_name_plural': 'Notice',
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Qualification',
                'ordering': ('qualification',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Toppers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('grade', models.CharField(blank=True, max_length=10, null=True)),
                ('photo', models.ImageField(upload_to='images/')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Nobles.Student')),
            ],
            options={
                'verbose_name_plural': 'Toppers',
            },
        ),
        migrations.AddField(
            model_name='faculty',
            name='qualification',
            field=models.ManyToManyField(to='Nobles.Qualification'),
        ),
    ]

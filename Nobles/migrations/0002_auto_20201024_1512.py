# Generated by Django 2.1.7 on 2020-10-24 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nobles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ('publish',), 'verbose_name_plural': 'Notice'},
        ),
    ]
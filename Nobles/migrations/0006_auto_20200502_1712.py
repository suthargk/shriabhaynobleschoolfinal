# Generated by Django 2.1.7 on 2020-05-02 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nobles', '0005_auto_20200430_1726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['cid'], 'verbose_name_plural': 'Classroom'},
        ),
    ]
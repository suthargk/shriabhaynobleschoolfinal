# Generated by Django 2.1.7 on 2020-08-06 06:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning', '0002_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

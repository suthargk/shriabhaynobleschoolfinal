# Generated by Django 2.1.7 on 2020-08-06 06:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning', '0003_auto_20200806_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 2.1.7 on 2020-04-30 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nobles', '0004_auto_20200430_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cid',
            field=models.IntegerField(null=True),
        ),
    ]
# Generated by Django 3.1.6 on 2021-02-25 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210225_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]

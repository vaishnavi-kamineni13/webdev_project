# Generated by Django 3.0.8 on 2020-08-25 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20200809_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='favourite',
        ),
    ]

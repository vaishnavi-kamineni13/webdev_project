# Generated by Django 3.0.8 on 2020-07-24 10:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0012_auto_20200720_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]

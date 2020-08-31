# Generated by Django 3.0.8 on 2020-07-20 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200720_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vnr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollnumber', models.CharField(max_length=10)),
                ('full_name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
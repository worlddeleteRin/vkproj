# Generated by Django 3.1.12 on 2021-06-15 18:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210615_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 18, 37, 30, 398922)),
        ),
    ]
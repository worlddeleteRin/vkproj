# Generated by Django 3.1.12 on 2021-06-15 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210614_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 14, 3, 57, 502933)),
        ),
    ]

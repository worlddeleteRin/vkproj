# Generated by Django 3.1.12 on 2021-06-14 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210614_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 3.1.12 on 2021-06-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_created_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

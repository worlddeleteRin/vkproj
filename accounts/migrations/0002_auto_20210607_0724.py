# Generated by Django 3.2.4 on 2021-06-07 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='like_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='reply_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='vk_id',
            field=models.IntegerField(),
        ),
    ]
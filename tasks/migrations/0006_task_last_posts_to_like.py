# Generated by Django 3.1.12 on 2021-06-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20210614_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='last_posts_to_like',
            field=models.IntegerField(default=0),
        ),
    ]

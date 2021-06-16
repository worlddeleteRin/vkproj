# Generated by Django 3.1.12 on 2021-06-15 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_task_groups_list_thief'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default=None, max_length=300)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]

# Generated by Django 4.2 on 2023-05-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_rename_user_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completion_date',
            field=models.CharField(default='not compleate', max_length=20),
        ),
    ]
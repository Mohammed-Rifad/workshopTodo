# Generated by Django 4.2 on 2023-05-03 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Task',
        ),
    ]

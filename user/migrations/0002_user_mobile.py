# Generated by Django 4.2 on 2023-05-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.BigIntegerField(default=0),
        ),
    ]

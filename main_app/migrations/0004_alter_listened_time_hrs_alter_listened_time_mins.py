# Generated by Django 4.1.3 on 2022-11-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_listened_time_listened_time_hrs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listened',
            name='time_hrs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listened',
            name='time_mins',
            field=models.IntegerField(default=0),
        ),
    ]

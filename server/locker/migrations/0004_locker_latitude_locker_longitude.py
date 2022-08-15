# Generated by Django 4.1 on 2022-08-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0003_alter_locker_end_time_alter_locker_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='locker',
            name='latitude',
            field=models.FloatField(default=35.835),
        ),
        migrations.AddField(
            model_name='locker',
            name='longitude',
            field=models.FloatField(default=128.75),
        ),
    ]

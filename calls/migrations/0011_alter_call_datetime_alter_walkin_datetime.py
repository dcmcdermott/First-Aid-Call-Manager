# Generated by Django 4.1.3 on 2022-11-22 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0010_alter_call_datetime_alter_walkin_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 22, 17, 54, 23, 849986), null=True),
        ),
        migrations.AlterField(
            model_name='walkin',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 22, 17, 54, 23, 850540), null=True),
        ),
    ]

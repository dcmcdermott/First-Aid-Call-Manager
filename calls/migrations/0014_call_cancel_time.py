# Generated by Django 4.1.3 on 2022-11-23 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0013_alter_call_datetime_alter_walkin_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='cancel_time',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]

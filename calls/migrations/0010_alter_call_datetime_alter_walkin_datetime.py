# Generated by Django 4.1.3 on 2022-11-22 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0009_alter_call_datetime_alter_walkin_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='walkin',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

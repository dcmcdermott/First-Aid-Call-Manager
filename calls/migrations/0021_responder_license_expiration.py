# Generated by Django 4.1.3 on 2022-12-08 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0020_alter_call_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='responder',
            name='license_expiration',
            field=models.DateField(blank=True, null=True),
        ),
    ]

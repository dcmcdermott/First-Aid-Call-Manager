# Generated by Django 4.1.3 on 2022-12-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0023_alter_minor_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='minor',
            name='consent_scan',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

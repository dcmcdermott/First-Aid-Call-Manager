# Generated by Django 4.1.3 on 2022-12-18 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0022_minor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minor',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]

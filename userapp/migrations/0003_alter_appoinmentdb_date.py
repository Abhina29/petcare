# Generated by Django 4.2.3 on 2023-08-05 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_appoinmentdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinmentdb',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_registerdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='requestdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('breed', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
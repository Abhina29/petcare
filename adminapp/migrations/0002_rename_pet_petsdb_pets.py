# Generated by Django 4.2.3 on 2023-07-19 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petsdb',
            old_name='pet',
            new_name='pets',
        ),
    ]
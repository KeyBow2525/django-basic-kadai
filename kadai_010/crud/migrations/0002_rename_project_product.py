# Generated by Django 5.0.7 on 2024-08-04 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Product',
        ),
    ]

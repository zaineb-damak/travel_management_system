# Generated by Django 4.2.10 on 2024-02-26 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='trip_package',
            new_name='package',
        ),
    ]
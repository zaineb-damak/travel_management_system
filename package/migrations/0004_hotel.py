# Generated by Django 4.2.10 on 2024-02-25 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0003_liked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='package.package')),
            ],
        ),
    ]
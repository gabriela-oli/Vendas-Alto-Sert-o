# Generated by Django 4.0.4 on 2022-06-01 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='cidade',
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-01 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_local_cidade_local_cidade_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='empresa',
            field=models.CharField(default=1, max_length=75),
            preserve_default=False,
        ),
    ]

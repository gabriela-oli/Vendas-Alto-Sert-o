# Generated by Django 4.0.5 on 2022-06-30 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_produto_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='valor',
        ),
        migrations.AddField(
            model_name='produto_empresa',
            name='valor',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0 on 2022-06-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=225)),
                ('cnpj', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=100)),
            ],
        ),
    ]

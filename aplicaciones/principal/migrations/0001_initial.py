# Generated by Django 3.0.6 on 2020-05-26 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=50, unique=True)),
                ('apellido_cliente', models.CharField(max_length=50)),
                ('direccion_cliente', models.CharField(max_length=70)),
                ('telefono_cliente', models.CharField(max_length=15)),
            ],
        ),
    ]

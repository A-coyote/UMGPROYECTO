# Generated by Django 3.0.6 on 2020-05-26 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=50, unique=True)),
                ('descripcion_categoria', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=50, unique=True)),
                ('precio_prod', models.FloatField()),
                ('cantidad_prod', models.PositiveIntegerField(blank=True, null=True)),
                ('id_categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.categoria')),
            ],
        ),
    ]
# Generated by Django 3.0.5 on 2020-04-10 02:31

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeUnit',
            fields=[
                ('gml_id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('unit_type', models.CharField(max_length=64)),
                ('unit_code', models.IntegerField()),
                ('unit_name', models.CharField(max_length=64)),
                ('poly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('ingestion_date', models.DateTimeField(blank=True, null=True)),
                ('satellite', models.CharField(max_length=3)),
                ('mode', models.CharField(max_length=8)),
                ('orbit_direction', models.CharField(max_length=10)),
                ('cloud_cover', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('polarisation_mode', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=2, null=True), blank=True, null=True, size=None)),
                ('product_type', models.CharField(max_length=8)),
                ('relative_orbit_number', models.IntegerField()),
                ('size', models.BigIntegerField()),
                ('coordinates', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('sensing_date', models.DateTimeField(blank=True, null=True)),
                ('is_downloaded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UpdateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date', models.DateTimeField()),
                ('status', models.SmallIntegerField()),
            ],
        ),
    ]

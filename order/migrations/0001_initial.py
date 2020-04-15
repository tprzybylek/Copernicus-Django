# Generated by Django 3.0.5 on 2020-04-10 02:32

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_mail', models.EmailField(max_length=254)),
                ('ordered_date_time', models.DateTimeField()),
                ('completed_date_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Waiting'), (1, 'Pending'), (2, 'Complete'), (3, 'Err')])),
                ('clip_extent', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('layers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=8), blank=True, null=True, size=None)),
                ('products', models.ManyToManyField(to='search.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Product')),
            ],
        ),
    ]
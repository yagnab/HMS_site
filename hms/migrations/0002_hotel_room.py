# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('street_num', models.CharField(max_length=10)),
                ('street_name', models.CharField(max_length=100)),
                ('town_name', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('cost_per_night', models.DecimalField(decimal_places=2, max_digits=8)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms.Hotel')),
            ],
        ),
    ]
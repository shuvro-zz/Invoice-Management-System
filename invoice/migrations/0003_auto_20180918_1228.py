# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20180918_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.Customer'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 09:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160121_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 21, 9, 56, 45, 288732, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hostprofile',
            name='host_create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 21, 9, 56, 45, 288732, tzinfo=utc)),
        ),
    ]

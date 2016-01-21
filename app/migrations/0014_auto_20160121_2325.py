# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 16:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20160121_2316'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type_of_food',
            new_name='Food_kinds',
        ),
        migrations.RenameField(
            model_name='foods',
            old_name='foodde_scribe',
            new_name='food_describe',
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 21, 16, 25, 41, 311294, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hostprofile',
            name='host_create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 21, 16, 25, 41, 312294, tzinfo=utc), editable=False),
        ),
    ]
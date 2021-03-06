# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0003_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign', models.CharField(max_length=120)),
                ('order', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=120)),
                ('orderitems', models.CharField(max_length=520)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('payway', models.CharField(max_length=10)),
                ('status', models.CharField(default='\u5f85\u652f\u4ed8', max_length=20)),
                ('trade_no', models.CharField(blank=True, max_length=120, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User')),
            ],
        ),
    ]

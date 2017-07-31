# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-14 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_account_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=32)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('customer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Role')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

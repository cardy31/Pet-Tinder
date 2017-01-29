# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-28 22:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('petswipe', '0002_auto_20170128_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='adoptWithMedical',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(default='test@tester.com', max_length=254),
        ),
        migrations.AddField(
            model_name='member',
            name='previousOwnership',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='swipedanimal',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='swipedanimal', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='member',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
    ]

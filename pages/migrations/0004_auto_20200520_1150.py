# Generated by Django 3.0.6 on 2020-05-20 06:05

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200518_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagesdetail',
            name='facebook_tracker',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}),
        ),
        migrations.AddField(
            model_name='pagesdetail',
            name='insatgram_tracker',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}),
        ),
        migrations.AlterField(
            model_name='addetails',
            name='searched_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

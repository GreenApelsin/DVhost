# Generated by Django 2.2.16 on 2020-12-12 21:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20201213_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 13, 0, 39, 23, 119874), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 13, 0, 39, 23, 119874), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 13, 0, 39, 23, 120875), verbose_name='Дата'),
        ),
    ]

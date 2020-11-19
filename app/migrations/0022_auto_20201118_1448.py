# Generated by Django 2.2.16 on 2020-11-18 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20201118_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='fileFILE',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 18, 14, 48, 32, 691025), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 18, 14, 48, 32, 691025), verbose_name='Дата'),
        ),
    ]
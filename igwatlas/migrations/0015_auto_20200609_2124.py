# Generated by Django 2.0.10 on 2020-06-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igwatlas', '0014_wavedata_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wavedata',
            name='period',
            field=models.FloatField(blank=True, null=True, verbose_name='Период ВВ в часах'),
        ),
    ]
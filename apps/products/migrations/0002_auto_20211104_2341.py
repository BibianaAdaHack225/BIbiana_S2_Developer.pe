# Generated by Django 3.1.7 on 2021-11-04 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalindicator',
            name='category_product',
        ),
        migrations.RemoveField(
            model_name='historicalindicator',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalmeasureunit',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalproduct',
            name='category_product',
        ),
        migrations.RemoveField(
            model_name='historicalproduct',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalproduct',
            name='measure_unit',
        ),
        migrations.DeleteModel(
            name='HistoricalCategoryProduct',
        ),
        migrations.DeleteModel(
            name='HistoricalIndicator',
        ),
        migrations.DeleteModel(
            name='HistoricalMeasureUnit',
        ),
        migrations.DeleteModel(
            name='HistoricalProduct',
        ),
    ]

# Generated by Django 3.1.7 on 2022-01-20 21:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense_manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalProvider',
            new_name='HistoricalSupplier',
        ),
        migrations.RenameModel(
            old_name='Provider',
            new_name='Supplier',
        ),
        migrations.RenameField(
            model_name='historicalmerma',
            old_name='money_loss',
            new_name='lost_money',
        ),
        migrations.RenameField(
            model_name='merma',
            old_name='money_loss',
            new_name='lost_money',
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-18 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financemodel',
            name='price',
        ),
        migrations.RemoveField(
            model_name='financemodel',
            name='processing_and_delivery',
        ),
        migrations.RemoveField(
            model_name='financemodel',
            name='sale_commission',
        ),
    ]

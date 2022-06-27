# Generated by Django 4.0.1 on 2022-06-27 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_transaction_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='tattoo_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='allergy',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='allergy'),
        ),
        migrations.AddField(
            model_name='cart',
            name='artist_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='artist_id'),
        ),
        migrations.AddField(
            model_name='cart',
            name='design_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='design_id'),
        ),
        migrations.AddField(
            model_name='cart',
            name='estimated_time',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='estimated_time'),
        ),
    ]

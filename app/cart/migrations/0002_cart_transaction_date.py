# Generated by Django 4.0.1 on 2022-06-27 03:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='transaction_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='transaction_date'),
        ),
    ]

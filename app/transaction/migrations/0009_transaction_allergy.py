# Generated by Django 4.0.1 on 2022-06-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0008_remove_transaction_numavail'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='allergy',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='allergy'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-06-16 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tattoo', '0006_tattoo_colored'),
    ]

    operations = [
        migrations.AddField(
            model_name='tattoo',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='description'),
        ),
    ]

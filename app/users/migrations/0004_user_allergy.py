# Generated by Django 4.0.1 on 2022-06-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='allergy',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='allergy'),
        ),
    ]
# Generated by Django 4.0.1 on 2022-06-15 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0004_remove_design_color_design_colored'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='design',
            name='colored',
        ),
    ]

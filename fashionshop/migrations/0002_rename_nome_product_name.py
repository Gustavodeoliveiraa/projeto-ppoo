# Generated by Django 5.0.6 on 2024-06-01 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fashionshop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='nome',
            new_name='name',
        ),
    ]

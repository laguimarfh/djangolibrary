# Generated by Django 4.0.2 on 2022-11-12 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jkk', '0005_alter_jkk_xarray'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jkk',
            old_name='xarray',
            new_name='x',
        ),
    ]

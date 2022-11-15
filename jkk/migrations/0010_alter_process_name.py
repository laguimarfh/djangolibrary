# Generated by Django 4.0.2 on 2022-11-14 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jkk', '0009_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='name',
            field=models.CharField(choices=[('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('S7', 'S7'), ('S8', 'S8'), ('S9', 'S9'), ('S10', 'S10'), ('S11', 'S11'), ('S12', 'S12'), ('RSCS', 'RSCS'), ('LSCS', 'LSCS')], help_text='Sealer Process list', max_length=4),
        ),
    ]

# Generated by Django 4.0.2 on 2022-11-24 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jkk', '0026_remove_jkks8_checkstatus_4_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='s8elements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.CharField(max_length=2)),
                ('mayor_element', models.CharField(max_length=300)),
                ('keypoint', models.CharField(max_length=300)),
                ('worktime', models.FloatField()),
                ('walktime', models.FloatField()),
                ('tolerance', models.FloatField()),
            ],
        ),
    ]

# Generated by Django 4.0.2 on 2022-11-07 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputcs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.FloatField(default=None)),
                ('timeoory', models.FloatField(default=None)),
            ],
        ),
    ]

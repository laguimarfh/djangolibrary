# Generated by Django 4.0.2 on 2022-11-15 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jkk', '0017_dailyjkk_dayadh_periodjkk_periodadh_checkjkk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkjkk',
            name='jkk_elements',
        ),
    ]

# Generated by Django 4.0.2 on 2022-11-15 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jkk', '0018_remove_checkjkk_jkk_elements'),
    ]

    operations = [
        migrations.CreateModel(
            name='stopwatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element', models.CharField(max_length=300)),
                ('timeelement', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='checkJkk',
        ),
    ]

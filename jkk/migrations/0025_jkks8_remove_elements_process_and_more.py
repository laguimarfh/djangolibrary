# Generated by Django 4.0.2 on 2022-11-24 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jkk', '0024_rename_name_periodjkk_period_sel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jkks8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_sel', models.CharField(choices=[('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th')], help_text='Period select', max_length=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('jkk_tm', models.CharField(max_length=200)),
                ('jkk_auditor', models.CharField(max_length=200)),
                ('periodadh', models.FloatField(blank=True, null=True)),
                ('step_1', models.CharField(max_length=300)),
                ('step_2', models.CharField(max_length=300)),
                ('step_3', models.CharField(max_length=300)),
                ('step_4', models.CharField(max_length=300)),
                ('step_5', models.CharField(max_length=300)),
                ('steptime_1', models.FloatField(blank=True, null=True)),
                ('steptime_2', models.FloatField(blank=True, null=True)),
                ('steptime_3', models.FloatField(blank=True, null=True)),
                ('steptime_4', models.FloatField(blank=True, null=True)),
                ('steptime_5', models.FloatField(blank=True, null=True)),
                ('steptol_1', models.FloatField(blank=True, null=True)),
                ('steptol_2', models.FloatField(blank=True, null=True)),
                ('steptol_3', models.FloatField(blank=True, null=True)),
                ('steptol_4', models.FloatField(blank=True, null=True)),
                ('steptol_5', models.FloatField(blank=True, null=True)),
                ('checkstatus_1', models.BooleanField(null=True)),
                ('checkstatus_2', models.BooleanField(null=True)),
                ('checkstatus_3', models.BooleanField(null=True)),
                ('checkstatus_4', models.BooleanField(null=True)),
                ('checkstatus_5', models.BooleanField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='elements',
            name='process',
        ),
        migrations.RemoveField(
            model_name='jkk',
            name='dailyprocess',
        ),
        migrations.RemoveField(
            model_name='periodjkk',
            name='auditor',
        ),
        migrations.RemoveField(
            model_name='periodjkk',
            name='checkelements',
        ),
        migrations.RemoveField(
            model_name='periodjkk',
            name='jkk_process',
        ),
        migrations.RemoveField(
            model_name='periodjkk',
            name='jkk_tm',
        ),
        migrations.DeleteModel(
            name='stopwatch',
        ),
        migrations.DeleteModel(
            name='elements',
        ),
        migrations.DeleteModel(
            name='Jkk',
        ),
        migrations.DeleteModel(
            name='periodJkk',
        ),
        migrations.DeleteModel(
            name='Process',
        ),
        migrations.DeleteModel(
            name='teamleader',
        ),
        migrations.DeleteModel(
            name='teamMember',
        ),
    ]
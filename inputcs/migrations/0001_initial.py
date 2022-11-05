# Generated by Django 4.0.2 on 2022-11-05 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process', models.CharField(choices=[('unknown', 'unknown'), ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('S7', 'S7'), ('S8', 'S8'), ('S9', 'S9'), ('S10', 'S10'), ('S11', 'S11'), ('S12', 'S12'), ('ED', 'ED')], max_length=30)),
                ('location', models.CharField(choices=[('RR DOOR OUTTER', 'Rear Door Outter'), ('RR DOOR INNER', 'Rear Door Inner'), ('RR DOOR PERIMETER', 'Rear Door Perimeter'), ('FR DOOR OUTTER', 'Front Door Outter'), ('FT DOOR INNNER', 'Front Door Inner'), ('FT DOOR PERIMETER', 'Front Door Perimeter'), ('HOOD', 'Hood'), ('HATCH', 'Hatch'), ('HATCH PEREMETER', 'Hatch Perimeter'), ('ROOF', 'Roof'), ('FENDER', 'Fender'), ('1/4 PANEL', '1/4 Panel'), ('C PILAR', 'C Pilar'), ('FUEL LID', 'Fuel Lid')], max_length=40)),
                ('defect', models.CharField(choices=[('XS', 'Excess'), ('WL', 'Waterleak'), ('PH', 'Pin Hole'), ('F', 'Flick'), ('ED R', 'ED run'), ('ED B', 'ED Blister'), ('NS', 'No Spat'), ('OF', 'Off Location'), ('MC', 'Missing Clip'), ('PA', 'Poor Application'), ('NB', 'No Brush'), ('G', 'Gap'), ('MAS', 'Mastic'), ('BB', 'Body Bound')], max_length=30)),
                ('side', models.CharField(choices=[('LH', 'Left Hand'), ('RH', 'Right Hand')], max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('period', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th')], max_length=30)),
                ('coorx', models.FloatField(default=None)),
                ('coory', models.FloatField(default=None)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ['defect', '-created'],
            },
        ),
    ]
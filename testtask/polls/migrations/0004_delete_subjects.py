# Generated by Django 4.0.6 on 2022-09-14 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_subjects_geo_lat_alter_subjects_geo_lon'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subjects',
        ),
    ]

# Generated by Django 4.1.4 on 2023-02-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_arduino_check_filled'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin_status',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='bin_status',
            name='location_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='camera_vision',
            name='location_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
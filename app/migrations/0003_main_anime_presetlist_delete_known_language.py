# Generated by Django 4.1.4 on 2022-12-27 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_known_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='main_anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Y', 'filled'), ('N', 'notfilled')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PresetList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='known_Language',
        ),
    ]

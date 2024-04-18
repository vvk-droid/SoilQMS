# Generated by Django 4.2.4 on 2024-04-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SoilQMS', '0006_usercrophistory_moisture_usercrophistory_nutrients_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crop',
            old_name='nutrients',
            new_name='humidity',
        ),
        migrations.RenameField(
            model_name='usercrop',
            old_name='nutrients',
            new_name='humidity',
        ),
        migrations.RenameField(
            model_name='usercrophistory',
            old_name='nutrients',
            new_name='humidity',
        ),
        migrations.RemoveField(
            model_name='usercrophistory',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='crop',
            name='nitrogen',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='phosphorous',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crop',
            name='potassium',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercrop',
            name='nitrogen',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercrop',
            name='phosphorous',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercrop',
            name='potassium',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercrophistory',
            name='nitrogen',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercrophistory',
            name='phosphorous',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercrophistory',
            name='potassium',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]

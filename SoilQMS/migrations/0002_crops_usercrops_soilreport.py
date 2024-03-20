# Generated by Django 4.2.5 on 2024-03-20 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SoilQMS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('ph_value', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('nutrients', models.IntegerField()),
                ('moisture', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserCrops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph_value', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('nutrients', models.IntegerField()),
                ('moisture', models.IntegerField()),
                ('ideal_crop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_measured_values', to='SoilQMS.crops')),
            ],
        ),
        migrations.CreateModel(
            name='SoilReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='SoilQMS.usercrops')),
            ],
        ),
    ]
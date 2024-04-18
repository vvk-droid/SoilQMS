from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Crop(models.Model):
    name = models.CharField(max_length=64)
    ph_value = models.FloatField()
    nitrogen = models.FloatField()
    phosphorous = models.FloatField()
    potassium = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    moisture = models.FloatField()


class UserCrop(models.Model):
    ideal_crop = models.OneToOneField(Crop, on_delete=models.CASCADE, related_name='user_measured_values')
    ph_value = models.FloatField()
    nitrogen = models.FloatField()
    phosphorous = models.FloatField()
    potassium = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    moisture = models.FloatField()


class UserCropHistory(models.Model):
    crop = models.ForeignKey(UserCrop, on_delete=models.CASCADE, related_name='reports')
    ph_value = models.FloatField()
    nitrogen = models.FloatField()
    phosphorous = models.FloatField()
    potassium = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    moisture = models.FloatField()

    class Meta:
        verbose_name_plural = "UserCropHistory"

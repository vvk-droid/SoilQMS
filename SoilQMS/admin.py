from django.contrib import admin
from .models import User, Crop, UserCrop, UserCropHistory

# Register your models here.
admin.site.register(User)
admin.site.register(Crop)
admin.site.register(UserCrop)
admin.site.register(UserCropHistory)

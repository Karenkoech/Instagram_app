from django.contrib import admin
from .models import Image, Profile

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Image)
admin.site.register(Profile)
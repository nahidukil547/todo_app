from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Todo)
admin.site.register(models.Profile)

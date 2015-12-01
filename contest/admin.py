from django.contrib import admin

from .models import *

class ApplicationAdmin(admin.ModelAdmin):
    model = Application

admin.site.register(Application, ApplicationAdmin)

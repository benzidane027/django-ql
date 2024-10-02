from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import profile

class ProfileAdmin(admin.ModelAdmin):
    pass
    
    
admin.site.register(profile, ProfileAdmin)

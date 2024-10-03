from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import profile

class ProfileAdmin(admin.ModelAdmin):
    #this class use to show all field in admin page
    pass
    
    
admin.site.register(profile, ProfileAdmin)

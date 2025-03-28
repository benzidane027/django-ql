from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import profile

class ProfileAdmin(admin.ModelAdmin):
    #this class use to show all field in admin page
    readonly_fields = ('date_joined','last_login','image_uid',"username")
    
    
admin.site.register(profile, ProfileAdmin)

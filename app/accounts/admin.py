from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import profile


admin.site.register(profile, UserAdmin)

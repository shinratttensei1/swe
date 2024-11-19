from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Define fields to display in the admin list
    list_display = ('username', 'email', 'role', 'is_active', 'is_approved')
    list_filter = ('role', 'is_active', 'is_approved')
    search_fields = ('username', 'email')

    # Fields to edit in the admin interface
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'is_approved')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

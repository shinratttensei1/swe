from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'is_approved')  # Display these columns
    list_filter = ('role', 'is_active', 'is_approved')  # Add filters for quick searches
    search_fields = ('username', 'email')  # Allow search by username and email

    # Define custom actions
    actions = ['approve_selected_farmers', 'reject_selected_farmers']

    # Approve farmers
    @admin.action(description="Approve selected farmers")
    def approve_selected_farmers(self, request, queryset):
        count = queryset.filter(role='farmer', is_approved=False).update(is_approved=True)
        self.message_user(request, f"{count} farmers approved successfully.")

    # Reject farmers
    @admin.action(description="Reject (delete) selected farmers")
    def reject_selected_farmers(self, request, queryset):
        count = queryset.filter(role='farmer').delete()
        self.message_user(request, f"{count[0]} farmers rejected and deleted.")

# Register the custom user admin
admin.site.register(CustomUser, CustomUserAdmin)
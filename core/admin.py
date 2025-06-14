from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Post

class CustomUserAdmin(BaseUserAdmin):
    # Define the fields to display in the admin interface
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    # Define the fields to search in the admin interface
    search_fields = ('id', 'username', 'email', 'first_name', 'last_name')
    # Define the fields to be read only in the admin interface
    readonly_fields = ('id', 'last_login', 'date_joined')
    # Define the fields to be displayed in the admin interface
    fieldsets = (
        (None, {'fields': ('id', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Post)

from django.contrib import admin
from .models import Book, User, Category, Transaction
from django.contrib.auth.admin import UserAdmin

# Extend UserAdmin to include 'role', 'date_of_membership', and 'active_status'
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Library Info', {'fields': ('role', 'date_of_membership', 'active_status')}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')


# Register your models here
admin.site.register(User, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Transaction)

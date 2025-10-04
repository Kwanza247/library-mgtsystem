from django.contrib import admin
from .models import Book, User, Category, Transaction
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Transaction)
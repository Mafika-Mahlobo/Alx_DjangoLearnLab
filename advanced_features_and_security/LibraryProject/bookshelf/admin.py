from django.contrib import admin
from .models import Book, CustomUser

class BoookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')
    list_filter = ('title', 'author', 'publication_year')


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    search_fields = ("username", "email")
    fieldsets = (

            (None, {"fields": ("username", "email", "password", "date_of_birth", "profile_phone")}),
            ("permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        )


admin.site.register(Book, BoookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

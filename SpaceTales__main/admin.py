from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username", "first_name", "last_name", "email", "phone",
    )
    search_fields = ("username", "email")
    list_filter = ("username", "email")


admin.site.register(models.User, CustomUserAdmin)
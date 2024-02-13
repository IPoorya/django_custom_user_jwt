from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["username", "phone_number", "email",
                    "date_joined", "last_login", "is_admin"]
    list_filter = ["date_joined", "last_login", "is_admin"]
    readonly_fields = ["date_joined", "last_login"]
    fieldsets = [
        (None,
         {
             "fields": ["phone_number", "username", "email", "password"]}),
        ("Permissions",
         {
             "fields": ["is_admin", "is_active", "date_joined", "last_login"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["phone_number", "username", "email", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["username", "phone_number", "email"]
    ordering = []
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
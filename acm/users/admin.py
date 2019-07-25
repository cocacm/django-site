from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ACMUserCreationForm, ACMUserChangeForm
from .models import ACMUser


class CustomUserAdmin(UserAdmin):
    add_form = ACMUserCreationForm
    form = ACMUserChangeForm
    model = ACMUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio',
                           'sid', )}),
    )


admin.site.register(ACMUser, CustomUserAdmin)

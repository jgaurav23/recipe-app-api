""" Django admin Customizarion """

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    """ Define the user pages for users. """
    list_display = ['email', 'name', 'is_staff', 'is_active']
    search_fields = ('email', 'name')
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),      # None refers to title of the section in admin page
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ('last_login',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),       # A CSS classes for fields look quiet wide.
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


admin.site.register(models.User, UserAdmin)

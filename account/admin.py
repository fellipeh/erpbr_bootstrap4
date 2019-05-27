# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('first_name', 'email', )
    # list_filter = ('is_admin',)

    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     # ('Personal info', {'fields': ('date_of_birth',)}),
    #     ('Permissions', {'fields': ('is_admin',)}),
    # )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2')}
    #      ),
    # )
    search_fields = ('username', 'first_name', 'email')
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)

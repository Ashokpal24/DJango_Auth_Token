from django.contrib import admin
from Auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'name', 'dob', 'is_admin', 'is_active')
    list_filter = ('is_admin', 'is_active')
    # visible fields in admin view
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal Informatiom', {'fields': ('name', 'dob')}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Status', {'fields': ('is_active',)})
    )
    # visible fields when adding new users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'dob', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ()


admin.site.register(User, UserModelAdmin)

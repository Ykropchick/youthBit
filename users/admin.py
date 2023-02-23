from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Department


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'password', 'firstname', 'lastname', 'department', 'is_HR',
                    'HR_link', 'start_date', 'is_started', 'is_staff', 'is_active',)
    list_filter = ('email', 'department', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'firstname', 'lastname', 'department', 'is_HR',
                           'HR_link', 'is_started',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Department)

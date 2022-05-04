from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('registration_number', 'email', 'password')
    search_fields = ('registration_number', 'email')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ('last_login',)
    fieldsets = ()
    ordering = ('email',)
    add_form = CustomUserForm
    change_form = PasswordChangingForm
    form = AccountEditForm
    model = CustomUser
    add_fieldsets = ((None, {'fields': 
    ('registration_number', 'password', 'confirm_password')}),
    ('Personal info', {'fields': ('registration_number', 'email','date_joined')}),
    ('Permissions', {'fields': ('is_active','is_staff')}),)



admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterUserForm, UserChangeForm
from .models import CustomUser


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = RegisterUserForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['username', 'email',]

admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,

)

# Register your models here.

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User


admin.site.register(User, CustomUserAdmin)

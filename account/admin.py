from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel
# Register your models here.
@admin.register(CustomUserModel)
class CustomAdmin(UserAdmin):
    model=CustomUserModel
    list_display=('username','email')
    fieldsets = UserAdmin.fieldsets+(
        ('Change picture',{
            'fields':['picture']
        }),
    )


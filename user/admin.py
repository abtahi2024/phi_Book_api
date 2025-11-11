from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model=User
    list_display=('email','first_name','last_name','profile_image','is_active')
    list_filter=('is_staff','is_active')

    fieldsets=(
        (None,{'fields':('email','password')}),
        ('Personal Info',{'fields':('first_name','last_name','address','phone_number','profile_image')}),
        ('Permissions', {'fields':('is_staff','is_active','is_superuser','groups','user_permissions')}),
        ('Important Dates',{'fields':('last_login','date_joined')})
    )

    add_fieldsets=((
        None,{
            'classes':('wide'),
            'fields':('email','password1','password2','is_staff','is_active', 'profile_image')
        }),
    )
    search_fields = ( "email",)
    ordering = ("email",)

admin.site.register(User,CustomUserAdmin)
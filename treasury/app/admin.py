from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):

    list_display = ('first_name','last_name','email','is_staff', 'is_active',)
    list_filter = ('first_name','email', 'is_staff', 'is_active',)

    search_fields = ('email','first_name','last_name','a1','a2','city','state','pincode')
    ordering = ('first_name',)

    add_fieldsets = (
        ('Personal Information', {
            # To create a section with name 'Personal Information' with mentioned fields
            'description': "",
            'classes': ('wide',),  # To make char fields and text fields of a specific size
            'fields': (('first_name','last_name'),'email','a1','a2','city','state','pincode','check',
                       'password1', 'password2',)}
        ),
        ('Permissions',{
            'description': "",
            'classes': ('wide', 'collapse'),
            'fields':( 'is_staff', 'is_active','date_joined')}),
    )

    def add_view(self,request, form_url='', extra_context=None):

        extra_context = {'title': 'see app_admin'}

        return super(CustomUserAdmin, self).add_view(request,form_url, extra_context=extra_context)
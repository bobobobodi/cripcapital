from django.contrib import admin
from .models import Transfer



class UserAdmin(admin.ModelAdmin):

    list_display = [
        'author',
        'money',
        'date_off',
        'money_off'
    ]

admin.site.register(Transfer, UserAdmin)


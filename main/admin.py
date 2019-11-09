from django.contrib import admin
from .models import UserUrl


class UserUrlAdmin(admin.ModelAdmin):
    list_display = ['id', 'long_url', 'short_url']


admin.site.register(UserUrl, UserUrlAdmin)

from django.contrib import admin
from .models import Shorter

@admin.register(Shorter)
class ShorterAdmin(admin.ModelAdmin):
    list_display = ('long_url', 'short_url', 'created', 'times_followed')

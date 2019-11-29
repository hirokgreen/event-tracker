from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'url',)
    search_fields = ('name', 'alias', 'url',)

admin.site.register(Event, EventAdmin)
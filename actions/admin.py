from django.contrib import admin
from .models import Actions
# Register your models here.

@admin.register(Actions)
class ActionAdmin(admin.ModelAdmin):
    list_display = ['user','verb','target','created']
    list_filter = ['created']
    search_fields = ['verb']
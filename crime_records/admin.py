from django.contrib import admin
from .models import CrimeRecord

# Register your models here.

class CrimeRecordAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'middle_name', 'created']
    list_filter = ['created', 'first_name', 'last_name', 'middle_name']

admin.site.register(CrimeRecord)

from django.contrib import admin
from .models import CrimeRecord, SentencingInfo


class SentencingInfoInline(admin.StackedInline):
    model = SentencingInfo
    can_delete = True
    verbose_name_plural = 'SentencingInfo'
    fk_name = 'criminal'


@admin.register(CrimeRecord)
class CrimeRecordAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'middle_name', 'created']
    list_filter = ['created', 'first_name', 'last_name', 'middle_name']
    inlines = (SentencingInfoInline,)

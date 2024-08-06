from django.contrib import admin
from .models import Code
# Register your models here.
admin.site.register(Code)
class CodeAdmin (admin.ModelAdmin):
    list_display = ('name','id')
    list_filter = ['created_at']
    list_per_page = 10
    search_fields = ['name']
    
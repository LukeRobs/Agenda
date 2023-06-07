from django.contrib import admin
from contact import models

@admin.register(models.contact)
class ContactAdmin(admin.ModelAdmin):
    
    list_display = 'id','first_name', 'last_name','office','city', 'phone', 'email',
    ordering = 'id',
    list_filter = ('city'),
    search_fields = 'first_name', 'city', 'email',
    list_per_page = 15
    list_max_show_all = 200

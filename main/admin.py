from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')
    readonly_fields = ('created_at', )
    list_display_links = ('id', 'name')
    search_fields = ('name', )








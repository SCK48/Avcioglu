from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite

from home.models import Setting, ContactFormMessage, FAQ


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'status', 'create_at', 'update_at']
    readonly_fields = ['name', 'phone', 'email', 'message', 'ip', 'create_at', 'update_at']



AdminSite.site_header = 'Avcıoğlu Tarım'
AdminSite.site_title = 'Avcıoğlu | Yönetim'
admin.site.register(Setting)
admin.site.register(FAQ)
admin.site.register(ContactFormMessage, MessageAdmin)
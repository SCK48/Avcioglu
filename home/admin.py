from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite

from home.models import Setting, ContactFormMessage, FAQ, SettingGallery


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'status', 'create_at', 'update_at']
    readonly_fields = ['name', 'phone', 'email', 'message', 'ip', 'create_at', 'update_at']

class GalleryInline(admin.TabularInline):
    model = SettingGallery
    extra = 1
    show_change_link = True

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'email']
    inlines = [GalleryInline]

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'setting', 'image']


AdminSite.site_header = 'Avcıoğlu Tarım'
AdminSite.site_title = 'Avcıoğlu | Yönetim'
admin.site.register(Setting, SettingAdmin)
admin.site.register(FAQ)
admin.site.register(SettingGallery,GalleryAdmin)
admin.site.register(ContactFormMessage, MessageAdmin)
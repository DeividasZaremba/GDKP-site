from django.contrib import admin

# Register your models here.

from .models import WowChar, WowClass, WowPlayer, WowSpec, CharInstance, EventRegistration

class WowCharInline(admin.TabularInline):
    model = WowChar
    extra = 0

class WowPlayerAdmin(admin.ModelAdmin):
    inlines = [WowCharInline]
    search_fields = ('id', 'nickname')

admin.site.register(WowChar)
admin.site.register(WowSpec)
admin.site.register(WowClass)
admin.site.register(CharInstance)
admin.site.register(EventRegistration)
admin.site.register(WowPlayer, WowPlayerAdmin)
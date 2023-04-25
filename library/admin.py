from django.contrib import admin

# Register your models here.

from .models import WowChar, WowClass, WowPlayer, WowSpec, CharInstance, EventRegistration
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class WowCharInline(admin.TabularInline):
    model = WowChar
    extra = 0

class WowPlayerAdmin(admin.ModelAdmin):
    inlines = [WowCharInline]
    search_fields = ('id', 'nickname')


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'get_groups', 'email', 'is_staff')

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    get_groups.short_description = 'Groups'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(WowChar)
admin.site.register(WowSpec)
admin.site.register(WowClass)
admin.site.register(CharInstance)
admin.site.register(EventRegistration)
admin.site.register(WowPlayer, WowPlayerAdmin)
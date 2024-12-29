from django.contrib import admin

from .models import Account, Channel, Group
# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number', 'birth_date')
    list_select_related = ('user', )

    def first_name(self, obj):
        return obj.user.first_name
    first_name.short_description = 'First name'

    def last_name(self, obj):
        return obj.user.last_name
    last_name.short_description = 'Last name'


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('title', 'username', 'link', 'created_date', 'is_private')
    list_select_related = ('user', )

    def username(self, obj):
        return obj.user.username
    username.short_description = 'Owner'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'username', 'link', 'created_date', 'is_private')
    list_select_related = ('user', )

    def username(self, obj):
        return obj.user.username
    username.short_description = 'Owner'
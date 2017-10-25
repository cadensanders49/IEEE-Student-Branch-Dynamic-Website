from django.contrib import admin
from .models import Event
from .models import Item
from .models import Member


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'funding']


admin.site.register(Event, EventAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount']


admin.site.register(Item, ItemAdmin)


class MemberAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'email', 'duesPaid']


admin.site.register(Member, MemberAdmin)

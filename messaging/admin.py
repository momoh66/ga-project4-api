from django.contrib import admin
from .models import Message
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'owner', 'recipient_parent')


admin.site.register(Message, MessageAdmin)

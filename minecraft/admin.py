from django.contrib import admin

from .models import MCModPack, MCServer

admin.site.register(MCServer)
admin.site.register(MCModPack)
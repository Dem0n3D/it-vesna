# -*- coding: UTF-8 -*-

from django.contrib import admin

from .models import *


class MenuAdmin(admin.ModelAdmin):
    model = Menu

class NodeAdmin(admin.ModelAdmin):
    model = Node

    list_display = ("title", "url", "order", "parent")

admin.site.register(Menu, MenuAdmin)
admin.site.register(Node, NodeAdmin)

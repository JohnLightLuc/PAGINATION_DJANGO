from django.contrib import admin

# Register your models here# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ContactAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'prenom', 'tel')
    list_filter = ('id', 'nom', 'prenom', 'tel')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)

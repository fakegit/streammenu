from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from django.utils.translation import ugettext_lazy as _
from streammenu.models import Menu


class StreamMenuModelAdmin(ModelAdmin):
    model = Menu
    menu_label = _('Stream Menus')
    menu_icon = 'link'
    list_display = ('name', 'slug', 'site')
    add_to_settings_menu = True

modeladmin_register(StreamMenuModelAdmin)

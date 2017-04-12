from django import template
from streammenu.models import Menu

register = template.Library()


@register.inclusion_tag('streammenu/menu.html', takes_context=True)
def render_menu(context, menu_slug):
    site = context['page'].get_site()
    try:
        menu = Menu.objects.get(site=site, slug=menu_slug)
    except Menu.DoesNotExist:
        return {'menu': {}}
    return {'menu': menu}

from django import template
from pages.models import Page

register = template.Library()

@register.inclusion_tag('pages/menu_list.html')
def show_menus():
	menu = Page.objects.all()
	return {'menu': menu}

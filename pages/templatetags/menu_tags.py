from django import template
from pages.models import Page

register = template.Library()

@register.inclusion_tag('pages/menu_list.html')
def main_menu():
	menu = Page.objects.filter(menu='HEAD').order_by('order_number')
	return {'menu': menu, 'menu_class': "main_menu"}

@register.inclusion_tag('pages/menu_list.html')
def side_menu():
	menu = Page.objects.filter(menu='SIDE').order_by('order_number')
	return {'menu': menu, 'menu_class': "side_menu"}

@register.inclusion_tag('pages/menu_list.html')
def bottom_menu():
	menu = Page.objects.filter(menu='BOTTOM').order_by('order_number')
	return {'menu': menu, 'menu_class': "bottom_menu"}





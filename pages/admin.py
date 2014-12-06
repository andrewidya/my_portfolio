from django.contrib import admin
from pages.models import Page
from mptt.admin import MPTTModelAdmin

# Register your models here.

class PageAdmin(MPTTModelAdmin):
	fieldsets = [
		('Page Information', {'fields': ['name', 'parent', 'author', 'menu']}),
	]
	list_display = ['name', 'author', 'permalink', 'menu']

admin.site.register(Page, PageAdmin)
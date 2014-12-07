from django.contrib import admin
from pages.models import Page
from mptt.admin import MPTTModelAdmin

# Register your models here.

class PageAdmin(MPTTModelAdmin):
	fieldsets = [
		('Page Information', {'fields': ['name', 'parent', 'menu', 'order_number']}),
	]
	list_display = ['name', 'author', 'permalink', 'menu', 'order_number']

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

admin.site.register(Page, PageAdmin)
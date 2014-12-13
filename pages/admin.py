from django.contrib import admin
from pages.models import Page
from mptt.admin import MPTTModelAdmin

# Register your models here.

class PageAdmin(MPTTModelAdmin):
	fieldsets = [
		('Page Information', {'fields': ['name', 'parent', 'menu', 'permalink']}),
		('Content Information', {'fields': ['content', 'pub_date', 'pub_status', 'page_type', 'order']}),
	]
	list_display = ['name', 'author', 'permalink', 'menu', 'pub_date', 'pub_status', 'modified_date', 'page_type', 'order']
	list_editable = ['order', 'pub_status']

	class Media:
		js = ('/static/content/js/tinymce/tinymce.min.js', '/static/content/js/tinymce/textarea.js',)

	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()

admin.site.register(Page, PageAdmin)
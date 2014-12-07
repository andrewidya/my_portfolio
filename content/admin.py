from django.contrib import admin
from content import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		('Post Content', {'fields': ['title', 'content', 'page']}),
		('Date & Status Information', {'fields': ['pub_date', 'pub_status', 'tag']})
	]

	list_filter = ['title', 'author', 'pub_date']
	list_display = ['title', 'author', 'pub_date', 'pub_status', 'modified_date', 'permalink']
	search_fields = ['title', 'author', 'pub_date', 'pub_status']
	filter_horizontal = ['tag',]
	date_hierarchy = 'pub_date'

	class Media:
		js = ('/static/content/js/tinymce/tinymce.min.js', '/static/content/js/tinymce/textarea.js',)

	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()


admin.site.register(models.Tag)
admin.site.register(models.Post, PostAdmin)
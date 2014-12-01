from django.contrib import admin
from comments.models import Comment
from mptt.admin import MPTTModelAdmin

# Register your models here.

class CommentAdmin(MPTTModelAdmin):
	list_display = ['post', 'content', 'author', 'date', 'status']

admin.site.register(Comment, CommentAdmin)
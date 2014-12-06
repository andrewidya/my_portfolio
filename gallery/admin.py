from django.contrib import admin
from gallery.models import Album, Tag, Image

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "images"]

class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]

class ImageAdmin(admin.ModelAdmin):
    # search_fields = ["title"]

    fieldsets = [
    	('Image Information', {'fields': ['title', 'image', 'user', 'tags', 'albums', 'rating' ]})
    ]

    list_display = ["title", "__unicode__", "user", "rating", "size", "thumbnail", "created", "tags_"]
    list_filter = ["tags", "albums", "user"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
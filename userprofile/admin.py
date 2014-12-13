from django.contrib import admin
from userprofile.models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	fieldsets = [
		('Profile Picture', {'fields': ['avatar']}),
		('Home Information', {'fields': ['street', 'city', 'state', 'country']}),
		('About Yourself', {'fields': ['about']})
	]
	list_display = ['thumbnail', 'user_name']

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super(UserProfile, self).save(request, obj, form, change)

admin.site.register(UserProfile, UserProfileAdmin)
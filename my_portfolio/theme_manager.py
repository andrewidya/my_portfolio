from django.conf import settings

def theme_resolver(template):
	if settings.SYSTEM_THEMES and settings.SYSTEM_THEMES != '':
		return "%s/%s" % (settings.SYSTEM_THEMES, template)
	else:
		return "default/%s" % template
from django.conf import settings

def theme_resolver(theme):
	if settings.SYSTEM_THEMES and settings.SYSTEM_THEMES != '':
		return "%s/%s" % (settings.SYSTEM_THEMES, theme)
	else:
		return "default/%s" % theme
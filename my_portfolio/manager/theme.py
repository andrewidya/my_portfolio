from my_portfolio.settings import GLOBAL_THEMES

THEMES = GLOBAL_THEMES

def theme_loader(template):
	if not THEMES:
		return 'themes/defaults/%s' % template
	else:
		return 'themes/%s/%s' % (THEMES, template)
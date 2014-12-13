from django.shortcuts import render, get_object_or_404
from pages.models import Page
from my_portfolio.theme_manager import theme_resolver

# Create your views here.

def page(request, url):
	page = Page.objects.get(permalink=url)
	if page.page_type == "ABOUT":
		template = theme_resolver('about.html')
	if page.page_type == "CONTACT":
		template = theme_resolver('contact.html')
	else:
		template = theme_resolver('flatpage.html')
	context = {'post': page}
	return render(request, template, context)
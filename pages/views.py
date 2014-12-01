from django.shortcuts import render
from content.models import Post
from pages.models import Page
from django.http import HttpResponse
from my_portfolio.manager.theme import theme_loader

# Create your views here.

def page_index(request, url):
	page = Page.objects.all().filter(permalink=url)
	post = Post.objects.all().filter(page=page)
	if not post:
		return HttpResponse("Error, now content here")

	context = {'contents': post}
	template = theme_loader('index.html')
	return render(request, template, context)

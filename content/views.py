from django.shortcuts import render
from django.http import HttpResponse
from content.models import Post, Tag
from my_portfolio.manager.theme import theme_loader
from pages.models import Page

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def single_post(request, url, year, month, post_id, permalink):
	content = Post.objects.get(id=post_id)
	context = {'contents': content, 'document_title': content.title}
	print(url)
	print("single_post_method")
	template = theme_loader('single.html')
	return render(request, template, context)

def archive(request, url):
	page = Page.objects.get(permalink__exact=url[:-1])
	post = Post.objects.filter(page=page)
	print(url)
	print(page)
	#print(post.page.permalink)
	print("asu")
	if not post:
		return HttpResponse("Error, now content here")

	context = {'contents': post}
	template = theme_loader('index.html')
	return render(request, template, context)
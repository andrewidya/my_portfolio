from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from content.models import Post, Tag
from my_portfolio.manager.theme import theme_loader
from pages.models import Page

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def get_post(request, url, year, month, post_id, permalink):
	post = Post.objects.get(id=post_id)
	context = {'post': post, 'document_title': post.title}
	template = theme_loader('single.html')
	return render(request, template, context)

def archive(request, url):
	page = get_object_or_404(Page, permalink=url)
	print(page)
	post = get_list_or_404(Post, page=page)
	print(post)
	context = {'post': post, 'document_title': str(page.name) + str(" Archives") }
	return render(request, theme_loader('index.html'), context)

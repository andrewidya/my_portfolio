from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from django.http import HttpResponse
from content.models import Post, Tag
from pages.models import Page

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def get_post(request, url, year, month, post_id, permalink):
	post = Post.objects.get(id=post_id)
	context = {'post': post, 'document_title': post.title}
	return render(request, 'content/single.html', context)

def archive(request, url):
	page = get_object_or_404(Page, permalink=url)
	try:
		post = Post.objects.filter(page=page).filter(pub_status=True)
	except Post.DoesNotExist:
		raise Http404
	post = get_list_or_404(Post, page=page)
	context = {'post': post, 'document_title': str(page.name) + str(" Archives") }
	return render(request, 'content/index.html', context)

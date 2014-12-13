from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from content.models import Post, Tag, Category
from my_portfolio.theme_manager import theme_resolver

# Create your views here.
#

def index(request):
	return render(request, theme_resolver('homepage.html'))

def get_post_list(request):
    try:
    	post_query = Post.objects.filter(pub_status=True)
        paginator = Paginator(post_query, 2)
        page = request.GET.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)
    except Post.DoesNotExist:
    	raise Http404
    context = {'post': post_list}
    return render(request, theme_resolver('index.html'), context)

def get_post(request, year, month, post_id, permalink):
	post = Post.objects.get(id=post_id)
	context = {'post': post, 'document_title': post.title}
	return render(request, theme_resolver('single.html'), context)

def get_category(request):
	category = Category.objects.all()
	context = {'categories': category}
	return render(request, theme_resolver('index.html'), context)

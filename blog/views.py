from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
	{
		'author': 'CoreyMS',
		'title': 'Blog post 1',
		'content': 'First post',
		'date_posted': 'August 8, 2021'
	},
	{
		'author': 'Jane doe',
		'title': 'Blog post 2',
		'content': 'Second post',
		'date_posted': 'August 8 2000'
	}
]

def home(request):
	context = {
		'posts' : posts
	}

	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About title'})
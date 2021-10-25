from django.urls import path 

from . import views

urlpatterns = [
	# name property use for navigation url in html page: {% url 'blog-home' %}
	path('', views.home, name='blog-home'),
	path('about/', views.about, name='blog-about'),
]
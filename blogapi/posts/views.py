from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 

# Create your views here.
from rest_framework import generics, permissions
from .models import Post 
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
	# permission_classes = [permissions.IsAuthenticated]
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	# permission_classes  = (permissions.IsAuthenticated,) # must have comma at the end
	permission_classes = (IsAuthorOrReadOnly, )
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class HomePageView(View):
	def get(self, request):
		html = '<h1>This is home page</h1>'
		return HttpResponse(html)
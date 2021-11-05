from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import generics, permissions, serializers
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import CustomUser
from .serializers import UserSerializer 

class UserList(generics.ListAPIView):
	# permission_classes = [permissions.IsAuthenticated]
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer

@api_view(['POST',])
@permission_classes([permissions.AllowAny])
def registration_view(request):
	if request.method == 'POST':
		serializer = UserSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			user = serializer.save()

			data['response'] = 'successfully registered a new user'
			data['email'] = user.email
			data['username'] = user.username
		else:
			data = serializer.errors
		return Response(data)
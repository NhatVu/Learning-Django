from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import generics, permissions, serializers
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Account
from .serializers import UserSerializer 
from rest_framework.authtoken.models import Token

class UserList(generics.ListAPIView):
	# permission_classes = [permissions.IsAuthenticated]
	queryset = Account.objects.all()
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
			token = Token.objects.get(user=user).key
			data['token'] = token
		else:
			data = serializer.errors
		return Response(data)
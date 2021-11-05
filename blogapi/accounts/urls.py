from django.contrib.auth.models import User
from django.urls import path 
from .views import UserList, registration_view
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'accounts'

urlpatterns = [
	# path('<int:pk>/', PostDetail.as_view()),
	path('', UserList.as_view()),
	path('register', registration_view, name='register'),
	path('login', obtain_auth_token, name='login'),
]
from rest_framework import serializers
from .models import Post 

class PostSerializer(serializers.ModelSerializer):
	username = serializers.SerializerMethodField(method_name='get_username_from_author')
	
	class Meta:
		model = Post 
		fields = ('id', 'author', 'title', 'body', 'created_at', 'username')
		extra_kwargs = {'author': {'write_only': True}}
	
	def get_username_from_author(self, obj):
		username = obj.author.username
		return username
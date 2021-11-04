from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True) # change later
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return self.title

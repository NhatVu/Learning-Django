from django.db import models

# Create your models here.
class Todo(models.Model):
	# id field wil be automatically created by Django
	title = models.CharField(max_length=200)
	body = models.TextField()

	def __str__(self) -> str:
		return self.title

from django.db import models

# Create your models here.

class Task(models.Model):
	task_types = [
		('likes', 'likes'),
		('repost', 'repost'),	
	]
	t_type = models.CharField(default = None, 
	max_length = 300,
	choices = task_types)

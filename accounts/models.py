from django.db import models

# Create your models here.

class Account(models.Model):
	vk_id = models.IntegerField()
	username = models.CharField(default = None, max_length = 300,
	null = True, blank = True)
	password = models.CharField(default = None, max_length = 500,
	null = True, blank = True)
	access_token = models.CharField(default = None, max_length = 500,
	null = True, blank = True)
	created_time = models.IntegerField()
	last_used = models.IntegerField(default = 0)
	is_active = models.BooleanField(default = False)
	is_in_use = models.BooleanField(default = False)
	like_count = models.IntegerField()
	reply_count = models.IntegerField()

	def __str__(self):
		return str(self.vk_id)

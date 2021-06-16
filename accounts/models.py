from django.db import models
import time
from datetime import datetime

# Create your models here.

class Account(models.Model):
	vk_id = models.IntegerField()
	username = models.CharField(default = None, max_length = 300,
	null = True, blank = True)
	password = models.CharField(default = None, max_length = 500,
	null = True, blank = True)
	access_token = models.CharField(default = None, max_length = 500,
	null = True, blank = True)
	created_time = models.DateTimeField(default = datetime.now())
	created_source = models.CharField(default = None,
	max_length = 300,
	blank = True, null = True)
	last_used = models.DateTimeField(default = None)
	is_active = models.BooleanField(default = False)
	is_in_use = models.BooleanField(default = False)
	like_count = models.IntegerField()
	reply_count = models.IntegerField()

	def __str__(self):
		return str(self.vk_id)
	def set_used_time(self):
		self.last_used = datetime.fromtimestamp(int(time.time()))


def get_bots_to_use():
	a = Account.objects.filter(is_active = True)
	a = a.filter(is_in_use = True)
	a = a.order_by('last_used')
	return a


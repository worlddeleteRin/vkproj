from django.db import models
import time
from datetime import datetime
from accounts.models import * 
from vk_core.vk_core import * 
from useful_parameters import * 

# Create your models here.

class Task(models.Model):
	task_types = [
		('like_group_last_n_posts', 'like_group_last_n_posts'),
		('like_group_posts_list', 'like_group_posts_list'),
		('autopost_group_thief', 'autopost_group_thief'),
		('repost', 'repost'),
	]
	t_type = models.CharField(default = None,
	max_length = 300,
	choices = task_types)
	is_active = models.BooleanField(default =  True)
	is_infinite = models.BooleanField(default = True)
	frequency = models.IntegerField(default = 0)
	last_action_time = models.DateTimeField(default = None)
	admin_access_token = models.CharField(default = None,
		max_length = 300,
		blank = True, null = True)
	bots_use_count = models.IntegerField(default = 1)
	last_posts_to_like = models.IntegerField(default = 0)
	group_id = models.IntegerField(default = None,
	blank = True, null = True)
	groups_list_thief = models.TextField(default = None,
	null = True, blank = True)

	def time_to_make(self):
		if not self.last_action_time:
			return True
		now = int(time.time())
		time_past = now - self.last_action_time.timestamp().__int__()
		if time_past > self.frequency:
			return True
		return False
	def set_last_action_time_now(self):
		now = int(time.time())
		self.last_action_time = datetime.fromtimestamp(now)

class UsedData(models.Model):
	task =  models.ForeignKey(Task, on_delete = models.CASCADE)
	value = models.CharField(default = None,
	max_length = 300)

def is_data_used(task, data):
	was_used = UsedData.objects.filter(
		task = task,
		value = data,
	).exists()
	return was_used
def add_used_data(task, data):
	used_data = UsedData(
		task = task,
		value = data,
	)
	used_data.save()


def has_tasks():
	t = Task.objects.all().filter(is_active = True).__len__()
	if t > 0:
		return True
	return False
def active_tasks():
	active_tasks = Task.objects.all().filter(is_active = True)
	return active_tasks
def post_thief_first_nused(task, posts_list):
	post_to_use = None
	for post in posts_list:
		if is_data_used(task, post.id):
			pass
		else:
			post_to_use = post
			return post_to_use
	return post_to_use

	# get posts list (VkGroupPost objects)
	# and return first post from the list,
	# that was not used for current task

# END OF MODEL HELP METHODS
##################################


def make_tasks():
	print('start to make tasks')
	for task in active_tasks():
		if not task.time_to_make():
			return None
		if task.t_type == 'like_group_last_n_posts':
			like_group_last_n_posts(task)
		if task.t_type == 'autopost_group_thief':
			autopost_group_thief(task)
		# set last action time for each task
		task.set_last_action_time_now()
		task.save()
		# sleep after each task
		time.sleep(sleep_after_each_task)

def like_group_last_n_posts(task):
	print('*'*20)
	print('Start like last n posts task')
	print('*'*20)
	time.sleep(1)
	# task need to be make
	bots_to_use = get_bots_to_use()
	bots_to_use = bots_to_use[:task.bots_use_count]
	for bot in bots_to_use:
		print('user id is', bot.vk_id)
		client = VkClient()
		client.configure(bot.access_token)
		wall = VkWall(client, task.group_id, task.group_id)
		posts = wall.get_posts(task.last_posts_to_like)
		if not posts:
			return None
		for post in posts:
			post.like()
			time.sleep(3)
		# set actual bot use time and add like
		bot.set_used_time()
		bot.like_count += 1
		bot.save()

def autopost_group_thief(task):
	print('starting autopost task')
	# new group post to be made
	new_post = Post()
	new_post.attachments = []
	# configure client and main group wall
	client = VkClient()
	client.configure(task.admin_access_token)
	main_wall = VkWall(client, task.group_id, task.group_id)
	# get group ids list to thief
	groups_ids_thief = task.groups_list_thief.replace(' ', '').split(',')
	# get last 2 posts from each group
	posts_list = []
	for group_id in groups_ids_thief:
		current_wall = VkWall(client, group_id, group_id)
		current_posts = current_wall.get_posts(2)
		if not current_posts:
			pass
		posts_list += current_posts
	# sort posts by their date created, so the fresh are the first
	posts_list.sort(key=lambda post: post.date, reverse = True)
	# get the first post, that was not recently used
	post_to_use = post_thief_first_nused(task, posts_list)
	if not post_to_use:
		print('all posts from the list was already used!')
		return None
	#  add current post to thief to "used" posts
	add_used_data(task, post_to_use.id)
	# get all attachments (photos) from post to thief
	attachments_content_list = post_to_use.download_attachments()
	print('attachments list length is', attachments_content_list.__len__())
	for attachment_content in attachments_content_list:
		curr_photo = Photos(client)
		curr_photo.group_id = task.group_id
		curr_photo.photo_src = attachment_content
		curr_photo.upload_wall_photo()
		new_post.attachments.append(curr_photo.get_attachment_str())
	print('post attachments are', new_post.get_attachments_str())
	main_wall.post(new_post)






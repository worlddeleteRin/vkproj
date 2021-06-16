#!/usr/bin/python3
import time
import sys
import os
import django
from django.conf import settings

sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vkproj.settings')
django.setup()

from accounts.models import Account
from tasks.models import *
from useful_parameters import * 

if __name__ == '__main__':
	print('-' * 20)
	print('Starting bot!')
	print('-' * 20)
	sys.stdout.flush()
	while True:
		time.sleep(1)
		if has_tasks():
			print('has tasks, starting make them')
			sys.stdout.flush()
			make_tasks()
			print('all of the tasks are made!')
			sys.stdout.flush()
		else:
			print('no tasks, go sleep')
			sys.stdout.flush()
		time.sleep(sleep_after_tasks_done)

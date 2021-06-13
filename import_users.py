import os
import random
from timeit import default_timer as timer
import json

import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vkproj.settings')
django.setup()

from accounts.models import * 

users_file = open('users.json', 'r')
users = json.load(users_file)

for account in users['users']:
	if account["active"] == 'no':
		account_active = False
	else:
		account_active = True
	if account["in_use"] == 'no':
		account_use = False
	else:
		account_use = True
	new_account = Account(
		vk_id = account["id"],
		username = account["username"],
		password = account["password"],
		access_token = account["access_token"],
		created_time = account["start_working"],
		is_active = account_active,
		is_in_use = account_use,
		like_count = account["like"],
		reply_count = account["reply"],
	)
	new_account.save()



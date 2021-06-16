from django.contrib import admin
from .models import * 

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
	something = 12
	list_display = (
		"vk_id", 
		"username_password",
		"is_active",
		"is_in_use",
		"like_count",
		"reply_count",
		"last_used",
		"created_time",
		"created_source",
	)
	def username_password(self, obj):
		return obj.username + " : " + obj.password


admin.site.register(Account, AccountAdmin)

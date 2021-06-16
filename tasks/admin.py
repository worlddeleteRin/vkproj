from django.contrib import admin
from .models import * 

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
	list_display = (
	"t_type", 
	"is_active", 
	"is_infinite", 
	"bots_use_count", 
	"frequency",
	"last_action_time",
	)


admin.site.register(Task, TaskAdmin)

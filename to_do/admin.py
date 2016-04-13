from django.contrib import admin
from models import Todo_List
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
	list_display=('title', 'description',)

admin.site.register(Todo_List, TodoAdmin)
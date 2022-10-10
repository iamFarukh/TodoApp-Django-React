from django.contrib import admin
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ("title","description", "completed")

# Register the @admin.register()
admin.site.register(Todo,TodoAdmin)



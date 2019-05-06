from django.contrib import admin

# Register your models here.
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "state", "user", "published",)
	list_filter = ("state",)
	search_fields = ("title", "user__username",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ("body_short", "user",)
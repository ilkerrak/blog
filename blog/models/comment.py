from django.db import models
from django.contrib.auth.models import User
from .post import Post

class Comment(models.Model):
	class Meta:
		verbose_name = "Comment"
		verbose_name_plural = "Comments"
	user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
	body = models.TextField("Comment")
	reply = models.ForeignKey('self', verbose_name="Reply", on_delete=models.CASCADE, null=True, blank=True)
	post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)
	published = models.DateTimeField("Published Date", auto_now_add=True)

	def __str__(self):
		return self.body

	def body_short(self):
		max_len = 100
		return "{} ...".format(self.body[:max_len]) if len(self.body) > max_len else self.body
	body_short.short_description = "Comment"
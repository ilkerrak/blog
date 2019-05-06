from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posts"
	APPROVED = "approved"
	PENDING = "pending"
	PASSIVE = "passive"
	STATES = (
		(APPROVED, "Approved",),
		(PENDING, "Pending",),
		(PASSIVE, "Passive",),
	)
	user 	= models.ForeignKey(User, verbose_name="Publisher", on_delete=models.CASCADE)
	title 	= models.CharField("Title", max_length=155)
	state 	= models.CharField("State", max_length=24, choices=STATES, default=PENDING)
	published = models.DateTimeField("Published Date",)
	body 	= models.TextField("Content")

	def __str__(self):
		return self.title
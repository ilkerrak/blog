from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse

from .models import Post, Comment
# Create your views here.

def home_page(request):
	posts = Post.objects.filter(state=Post.APPROVED)
	return render(request, "home.html", dict(posts=posts))

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST": #request.POST:
		body = request.POST["body"]
		if body:
			if request.user.is_authenticated:
				comment, created = Comment.objects.get_or_create(
					user=request.user,
					body=body,
					post=post,
				)
				messages.success(request, "Your commnet has been submitted successfully")
			else:
				messages.warning(request, "You must login before submit comment!")
		else:
			messages.error(request, 'There is no content')
		return redirect(reverse('post_detail', kwargs=dict(pk=post.pk)))
	comments = Comment.objects.filter(post=post)
	return render(request, "post_detail.html", dict(post=post, comments=comments))
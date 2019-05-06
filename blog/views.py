from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse

from main.utils import paginate, get_query
from .models import Post, Comment
# Create your views here.

PER_PAGE = 6

def home_page(request):
	posts = Post.objects.filter(state=Post.APPROVED)
	q = request.GET.get("q")
	if q:
		entry_query = get_query(q, ("title",))
		posts = posts.filter(entry_query)
	posts = paginate(posts, per_page=PER_PAGE, page=request.GET.get("page"))
	return render(request, "home.html", dict(posts=posts))

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST": #request.POST:
		body = request.POST["body"]
		comment_id = request.POST.get("comment_id")
		if body:
			if request.user.is_authenticated:
				comment, created = Comment.objects.get_or_create(
					user=request.user,
					body=body,
					post=post,
					reply=Comment.objects.get(pk=comment_id) if comment_id and comment_id != "-1" else None,
				)
				messages.success(request, "Your commnet has been submitted successfully")
			else:
				messages.warning(request, "You must login before submit comment!")
		else:
			messages.error(request, 'There is no content')
		return redirect(reverse('post_detail', kwargs=dict(pk=post.pk)))
	comments = Comment.objects.filter(post=post, reply=None)
	return render(request, "post_detail.html", dict(post=post, comments=comments))
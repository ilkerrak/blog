from django.urls import path

from .views import post_detail

urlpatterns = [
    path('<int:pk>/', view=post_detail, name="post_detail"),
]
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post
from users.models import CustomUser

# Create your views here.
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('view_profile')

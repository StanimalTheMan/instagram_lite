from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect

from .forms import PostForm
from .models import Post
from users.models import CustomUser

# Create your views here.
class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post.html'
    success_url = reverse_lazy('view_profile')

    def get_success_url(self):
        return reverse('view_profile', kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/post_detail.html'
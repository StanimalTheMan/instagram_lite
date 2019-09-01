from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect

from .forms import PostForm, CommentForm
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

class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'picture',)
    template_name = 'posts/post_edit.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('view_profile')

    def get_success_url(self):
        return reverse('view_profile', kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'posts/add_comment_to_post.html', {'form': form})
from django.urls import path, re_path


from .views import CreatePostView, PostDetailView, PostUpdateView, PostDeleteView, add_comment_to_post


urlpatterns = [
    path('new/', CreatePostView.as_view(), name='add_post'),
    path('<uuid:pk>', PostDetailView.as_view(), name='post_detail'),
    path('<uuid:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<uuid:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<uuid:pk>/newcomment/', add_comment_to_post, name='add_comment_to_post'),
]
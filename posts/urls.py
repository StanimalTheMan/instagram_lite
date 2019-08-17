from django.urls import path, re_path


from .views import CreatePostView, PostDetailView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('new/', CreatePostView.as_view(), name='add_post'),
    path('<uuid:pk>', PostDetailView.as_view(), name='post_detail'),
    path('<uuid:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<uuid:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
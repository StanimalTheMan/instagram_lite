from django.urls import path, re_path


from .views import CreatePostView, PostDetailView


urlpatterns = [
    path('new/', CreatePostView.as_view(), name='add_post'),
    path('<uuid:pk>', PostDetailView.as_view(), name='post_detail'),
]
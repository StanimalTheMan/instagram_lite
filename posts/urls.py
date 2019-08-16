from django.urls import path


from .views import CreatePostView


urlpatterns = [
    path('post/', CreatePostView.as_view(), name='add_post'),
]
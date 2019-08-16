from django.urls import path, re_path


from .views import SignupPageView, view_profile


urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    re_path('(?P<username>[\w.@+-]+)/$', view_profile, name='view_profile'),
]
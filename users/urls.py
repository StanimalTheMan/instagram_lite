from django.urls import path, re_path


from .views import SignupPageView, MyLoginView, view_profile


urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('login/$', MyLoginView.as_view(), name='login'),
    re_path('(?P<username>[\w.@+-]+)/$', view_profile, name='view_profile'),
]
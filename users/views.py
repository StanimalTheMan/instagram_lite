from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model


from .forms import CustomUserCreationForm

# Create your views here.
class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def view_profile(request, username):
    profile = None
    CustomUser = get_user_model()

    try:
        profile = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        print("user does not exist")
    return render(request, 'profile/view_profile.html',{'profile':profile})
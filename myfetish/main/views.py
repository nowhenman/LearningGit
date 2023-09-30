from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.


def get_homepage(request):
    if request.session.session_key:
        return render(request, context={'user_logged_in': request.user.username}, template_name='main/homepage.html')
    return render(request, 'main/homepage.html')


def logout_user(request):
    logout(request)
    return render(request, 'main/homepage.html')

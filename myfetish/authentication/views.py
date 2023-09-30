from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm


# Create your views here.


def auth_sign_up(request):
    if request.method == 'POST':
        new_form = NewUserForm(request.POST)
        if new_form.is_valid():
            user = new_form.save()
            login(request, user)
            messages.success(request, message="Registration successful!")
        else:
            print(new_form.errors)
            for key, error in new_form.errors.items():
                for e in error:
                    messages.error(request, e)
            # messages.error(request, err_list)

    form = NewUserForm()
    return render(request, context={'reg_form': form}, template_name='authentication/sign_up.html')


def auth_login(request):
    if request.user.is_authenticated:
        return redirect("main:homepage")
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:homepage')
            else:
                print(form.errors)
                for key, error in form.errors.items():
                    for e in error:
                        messages.error(request, e)
                # messages.error(request, message='username or password is wrong')
        else:
            print(form.errors)
            for key, error in form.errors.items():
                for e in error:
                    messages.error(request, e)
            # messages.error(request, form.errors)

    form = AuthenticationForm()
    return render(request, context={'login_form': form}, template_name='authentication/login.html')

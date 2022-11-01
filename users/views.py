import re
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django import forms

from users.forms import UserProfileForm, UserForm

# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data['password1']
            
#             user = authenticate(username= username, password=password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})
# def login(request):
#     form = forms.LoginForm()
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         username = form.cleaned_data["username"]
#         password = form.cleaned_data['password1']
#         user = authenticate(username= username, password=password)
#         if form.is_valid():
#             login(request, user)
#     return render(request, 'registration/login.html', context={'form': form})

def register(request):
    form_user = UserForm()
    form_profile=UserProfileForm()
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile=UserProfileForm(request.POST, request.FILES)
        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')
    context={
        'form_user':form_user,
        'form_profile':form_profile
        }
    return render(request, 'users/register.html', context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    print(form)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')
    return render(request, 'users/login.html', {'form':form})
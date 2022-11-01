import re
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data['password']
            
            user = authenticate(username, password)
            login(request,user)
            return redirect('home')
        else:
            form = UserCreationForm()
            
            return render(request, 'registration/register.html', {'form': form})
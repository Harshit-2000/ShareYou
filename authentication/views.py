from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from . import forms
# Create your views here.


def signup_view(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    
    context = {
        'form' : form
    }

    return render(request, 'authentication/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')

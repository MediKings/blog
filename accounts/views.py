from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


User = get_user_model()

def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email):
            messages.warning(request, "Cette adresse email existe déjà")
            return redirect('accounts:register')
        else:
            user = User.objects.create_user(email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            if user:
                auth = authenticate(email=user.email, password=password)
                if auth is not None:
                    login(request, auth)
                    return redirect('accounts:login')
    return render(request, 'accounts/register.html', {})


def Login(request):
    username_email = request.POST.get('username_email')
    password = request.POST.get('password')
    if request.method=='POST':
        if(User.objects.filter(username=username_email).exists()):
            user = authenticate(username=username_email, password=password)
        elif(User.objects.filter(email=username_email).exists()):
            user = User.objects.get(email=username_email)
            user = authenticate(username=user.username, password=password)
        else:
            messages.error(request, "Données incorrects! Réessayez")
            return redirect('accounts:login')
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Mot de passe incorrects! Réessayez")
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


def Logout(request):
    logout(request)
    return redirect('accounts:login')
    
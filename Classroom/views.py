from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home_page(request):
    return render(request, 'Classroom/home_page.html')

def show_singin(request):
    return render(request, 'Classroom/Tela Sing in.html')


def submit_sing_in(request):
    if request.POST:
        verificar_usuario = request.POST.get('username')
        senha = request.POST.get('password')
        verificar = authenticate( usuario = verificar_usuario, password = senha)
        if verificar is not None:
            messages.error(request, "Usuario já Existente")
        else:
            try:
                User.objects.create_user(username = verificar_usuario, password = senha)
                return render(request, 'Classroom/home_page.html')
            except:
                messages.error(request, "Usuario já Existente")

    return redirect('/singin')


def login_user(request):
    return render( request, 'Tela Login.html')

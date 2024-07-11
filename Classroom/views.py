from msilib.schema import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Classroom.models import Dados
from functools import reduce
from django.db.models import Q
# Create your views here.

def home_page(request):
    return render(request, 'Classroom/home_page.html')

def show_singin(request):
    return render(request, 'Classroom/Tela Sing in.html')


def submit_sing_in(request):
    if request.POST:
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        verificar = authenticate( usuario = usuario, password = senha)
        if verificar is not None:
            messages.error(request, "Usuario já Existente")
        else:
            try:
                User.objects.create_user(username = usuario, password = senha)
                return render(request, 'Classroom/home_page.html')
            except:
                messages.error(request, "Usuario já Existente")

    return redirect('/singin')


def login_page(request):
    return render( request, 'Classroom/Tela Login.html')

def login_submit(request):
    if request.method == 'POST':
        usuario = request.POST.get("username")
        senha = request.POST.get('password')
        user = authenticate(request, username = usuario, password = senha)
        if user is not None:
            try:
                login(request, user)
                return render(request, 'Classroom/Tela Bem vindo.html')
            except:
            
                return render(request, 'Classroom/Tela Bem vindo.html')
        else:
            messages.error(request, "Usuario/Senha invalidos")
    return redirect('/login')


@login_required
def logout_user(request):
    logout(request)
    return redirect('/')

@login_required
def tela_cadastro(request):
    return render(request, 'Classroom/Tela Cadastro.html')


def cadastrar(request):
    if request.POST:
        cpf = request.POST.get( 'cpf' )
        nome = request.POST.get( 'nome' )
        matricula = request.POST.get( 'matricula' )
        nota1 = request.POST.get( 'nota1' )
        nota2 = request.POST.get( 'nota2' )
        try:
            Dados.objects.create(user=request.user, cpf=cpf, nome=nome, matricula=matricula,nota1=nota1, nota2=nota2)
        except:
            messages.error(request, "Dados Invalidos")
            return tela_cadastro(request)
    return redirect( '/' )


@login_required
def listar_aluno(request):
    dados = Dados.objects.filter(user=request.user)
    notas =[]

    for dado in dados:
        notas.append(dado.nota1)
        notas.append(dado.nota2)

    soma = lambda x, y: x + y

    soma_das_notas = reduce(soma, notas)
    
    numero_de_notas = len(notas)
    
    media = {'media': soma_das_notas / numero_de_notas}
    lista_dados = {'lista_dados' : dados,
                   'media': soma_das_notas / numero_de_notas} 
    
    return  render(request,'Classroom/Tela Listagem.html', lista_dados)


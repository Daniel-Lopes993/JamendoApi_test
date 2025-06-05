# Importações necessárias do Django
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Importa funções de serviço personalizadas
from .services import get_top_artists, get_top_tracks, get_track_info


# View protegida que retorna os artistas mais ouvidos do usuário logado
@login_required(login_url='login')  # Garante que o usuário esteja autenticado
def top_artists(request):
    limit = request.GET.get('limit', 10)  # Obtém o limite da query string, padrão é 10
    data = get_top_artists(limit)  # Chama serviço que retorna dados dos artistas
    return JsonResponse(data)  # Retorna os dados no formato JSON


# View protegida que retorna as músicas mais ouvidas do usuário logado
@login_required(login_url='login')
def top_tracks(request):
    limit = request.GET.get('limit', 10)
    data = get_top_tracks(limit)
    return JsonResponse(data)


# View protegida que retorna informações detalhadas de uma música específica
@login_required(login_url='login')
def track_info(request, track_id):
    data = get_track_info(track_id)  # Busca dados com base no ID da música
    return JsonResponse(data)


# Página inicial da aplicação, protegida por login
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


# View para login do usuário
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Autentica usuário
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)  # Loga o usuário
            return redirect('/')
        else:
            messages.info(request, 'Credenciais inválidas')  # Mostra erro
            return redirect('login')

    return render(request, 'login.html')  # Exibe o formulário de login


# View para cadastro de novo usuário
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # Verifica se email ou nome de usuário já estão em uso
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email já usado')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Nome de usuário já usado')
                return redirect('signup')
            else:
                # Cria novo usuário
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # Autentica e loga o novo usuário automaticamente
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('/')
        else:
            messages.info(request, 'Senhas não coincidem')
            return redirect('signup')
    else:
        return render(request, 'signup.html')  # Exibe o formulário de cadastro


# View para logout do usuário
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')  # Redireciona para a tela de login após sair

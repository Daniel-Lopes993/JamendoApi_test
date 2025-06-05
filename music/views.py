from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .services import get_top_artists, get_top_tracks, get_track_info

# Create your views here.



@login_required(login_url='login')
def top_artists(request):
    limit = request.GET.get('limit', 10)
    data = get_top_artists(limit)
    return JsonResponse(data)

@login_required(login_url='login')
def top_tracks(request):
    limit = request.GET.get('limit', 10)
    data = get_top_tracks(limit)
    return JsonResponse(data)

@login_required(login_url='login')
def track_info(request, track_id):
    data = get_track_info(track_id)
    return JsonResponse(data)

@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credenciais inválidas')
            return redirect('login')
        
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email já usado')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Nome de usuário ja usado')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # log user in 
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('/')
        else:
            messages.info(request, 'Senhas nao coincidem')
            return redirect('signup')
    else:    
        return render(request, 'signup.html')
    
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

"""
Configurações do projeto Django spotify_backend.

Gerado pelo comando 'django-admin startproject' usando Django 5.2.1.

Documentação oficial:
- Configurações básicas: https://docs.djangoproject.com/en/5.2/topics/settings/
- Referência completa das configurações: https://docs.djangoproject.com/en/5.2/ref/settings/
"""

# Importa a função config do pacote python-decouple para ler variáveis de ambiente de forma segura
from decouple import config

# Define a variável de ambiente JAMENDO_CLIENT_ID para usar na API do Jamendo
JAMENDO_CLIENT_ID = config('JAMENDO_CLIENT_ID')

# Importa biblioteca para facilitar configuração do banco de dados via URL
import dj_database_url

# Importa módulos para manipulação de caminhos e variáveis do sistema
from pathlib import Path
import os

# Define o diretório base do projeto (dois níveis acima do arquivo atual)
BASE_DIR = Path(__file__).resolve().parent.parent

# Alternativamente define JAMENDO_CLIENT_ID usando getenv, com valor padrão (serve se variável de ambiente não existir)
JAMENDO_CLIENT_ID = os.getenv('JAMENDO_CLIENT_ID', '7f8fee15')

# Configurações básicas do projeto:

# Chave secreta do Django usada para segurança (mantenha em segredo em produção)
SECRET_KEY = 'django-insecure-iq-rc$a(3#3gq&)qj-%op-gt*exd#vwv3_(#y7k05w$35sdw@o'

# Debug desativado para produção (não exibe erros detalhados para usuários finais)
DEBUG = False

# Define os hosts permitidos para acessar o projeto (domínios válidos)
ALLOWED_HOSTS = ['.onrender.com']  # Permite subdomínios do domínio onrender.com


# Configuração dos aplicativos instalados no projeto
INSTALLED_APPS = [
    'django.contrib.admin',          # Interface administrativa
    'django.contrib.auth',           # Sistema de autenticação
    'django.contrib.contenttypes',   # Permite trabalhar com tipos de dados do Django
    'django.contrib.sessions',       # Gerenciamento de sessões
    'django.contrib.messages',       # Mensagens temporárias
    'django.contrib.staticfiles',    # Gerenciamento de arquivos estáticos
    'music'                         # Aplicação customizada do projeto
]

# Middleware são camadas que processam requisições/respostas
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Segurança geral
    'django.contrib.sessions.middleware.SessionMiddleware',  # Gerencia sessões do usuário
    'django.middleware.common.CommonMiddleware',  # Algumas funcionalidades comuns para HTTP
    'django.middleware.csrf.CsrfViewMiddleware',  # Proteção contra ataques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Gerencia autenticação do usuário
    'django.contrib.messages.middleware.MessageMiddleware',  # Suporta mensagens flash
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protege contra clickjacking
]

# Arquivo que contém as URLs do projeto
ROOT_URLCONF = 'spotify_backend.urls'

# Configuração dos templates (arquivos HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Motor de templates do Django
        'DIRS': [BASE_DIR / 'templates'],  # Diretório onde ficam os templates do projeto
        'APP_DIRS': True,  # Busca templates dentro das pastas de apps instalados
        'OPTIONS': {
            'context_processors': [  # Variáveis automáticas disponíveis nos templates
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuração do WSGI para deployment
WSGI_APPLICATION = 'spotify_backend.wsgi.application'


# Configuração do banco de dados via URL (muito usado para deploy em serviços como Heroku)
DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL'))
}

# Validações padrão para senhas de usuários
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configurações de localização e idioma
LANGUAGE_CODE = 'en-us'  # Idioma padrão inglês dos EUA
TIME_ZONE = 'UTC'        # Fuso horário padrão UTC

USE_I18N = True  # Habilita internacionalização (traduções)
USE_TZ = True    # Usa timezone-aware datetimes


# Configuração para arquivos estáticos (CSS, JS, imagens)

STATIC_URL = '/static/'  # URL base para acessar arquivos estáticos

# Diretório onde arquivos estáticos serão coletados para produção
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Diretórios adicionais onde o Django buscará arquivos estáticos em desenvolvimento
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]

# Tipo padrão para campos auto-incrementados nas models (PK)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

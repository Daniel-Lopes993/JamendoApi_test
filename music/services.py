# Importa a biblioteca requests para fazer requisições HTTP
import requests

# Importa as configurações do Django (como variáveis do settings.py)
from django.conf import settings

# URL base da API do Jamendo
JAMENDO_API_URL = 'https://api.jamendo.com/v3.0'

# Obtém o CLIENT_ID do settings.py; caso não esteja definido, usa o valor padrão 'YOUR_CLIENT_ID'
CLIENT_ID = getattr(settings, 'JAMENDO_CLIENT_ID', 'YOUR_CLIENT_ID')


# Função que busca os artistas mais populares da API do Jamendo
def get_top_artists(limit=10):
    url = f"{JAMENDO_API_URL}/artists"  # Endpoint da API para artistas
    params = {
        'client_id': CLIENT_ID,         # ID do cliente (para autenticação na API)
        'format': 'json',               # Formato da resposta
        'limit': limit,                 # Quantidade máxima de artistas retornados
        'order': 'popularity_total'     # Ordena por popularidade total
    }
    response = requests.get(url, params=params)  # Realiza a requisição GET com os parâmetros
    return response.json()                       # Retorna a resposta no formato JSON


# Função que busca as músicas mais populares da API do Jamendo
def get_top_tracks(limit=10):
    url = f"{JAMENDO_API_URL}/tracks"  # Endpoint da API para faixas/músicas
    params = {
        'client_id': CLIENT_ID,
        'format': 'json',
        'limit': limit,
        'order': 'popularity_total'
    }
    response = requests.get(url, params=params)
    return response.json()


# Função que busca informações detalhadas de uma música específica pelo seu ID
def get_track_info(track_id):
    url = f"{JAMENDO_API_URL}/tracks"  # Mesmo endpoint de faixas
    params = {
        'client_id': CLIENT_ID,
        'format': 'json',
        'id': track_id                 # Define o ID da faixa específica a ser buscada
    }
    response = requests.get(url, params=params)
    return response.json()

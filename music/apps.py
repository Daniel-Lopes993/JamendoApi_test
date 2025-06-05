from django.apps import AppConfig

# Classe de configuração da aplicação "music"
class MusicConfig(AppConfig):
    # Define o tipo padrão para os campos auto-incrementados (Primary Key) nas models desta app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nome da aplicação (deve corresponder ao nome da pasta do app)
    name = 'music'


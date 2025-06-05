#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# Este é o *shebang*, que permite executar o script diretamente no terminal Unix/Linux.
# Ele diz ao sistema para usar o interpretador Python configurado no ambiente.

import os  # Módulo para interagir com variáveis de ambiente e o sistema operacional
import sys  # Módulo que permite acessar argumentos e funções relacionadas ao sistema


def main():
    """Função principal para execução de tarefas administrativas do Django."""
    
    # Define a variável de ambiente DJANGO_SETTINGS_MODULE, que aponta para o módulo de configurações do projeto
    # Aqui, o projeto está usando o arquivo de configuração localizado em 'spotify_backend/settings.py'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotify_backend.settings')
    
    try:
        # Importa a função que executa comandos administrativos do Django, como runserver, migrate, etc.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Lança um erro caso o Django não esteja instalado ou não esteja acessível
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Executa o comando passado na linha de comando, como:
    # python manage.py runserver
    execute_from_command_line(sys.argv)


# Verifica se este arquivo está sendo executado diretamente (e não importado como módulo)
if __name__ == '__main__':
    main()

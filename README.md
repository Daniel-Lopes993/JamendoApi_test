# 🎵 Jamendo API Django Integration

Este é um projeto **Django** com integração à **Jamendo API**, permitindo:

✅ Listar Top Artistas  
✅ Listar Top Músicas  
✅ Buscar informações de uma música específica  

Além disso, conta com:

✅ Sistema de autenticação (Login, Signup, Logout)  
✅ Integração com banco de dados PostgreSQL via **Neon**  
✅ Deploy automatizado na **Render**  
✅ Arquivos estáticos (CSS, imagens) servidos via Render

---

## 🚀 Tecnologias

- Python 3.11+
- Django 5.x
- PostgreSQL (Neon)
- Render.com (deploy)
- Gunicorn
- Requests (para consumir a API)
- Bootstrap (no frontend)

Disclaimer: ## Código utilizado foi criado pelo youtuber: @CodeWithTomi com mudanças para o uso da JamendoAPI


Os principais arquivos a ser analisado são o manage.py, music/views.py, music/services.py, music/urls.py e em spotify_backend/settings.py

Arquivos adicionais como o 'staticfiles' para o css e o 'templates' para o HTML estão utilizando urls externas como o bootstrap no css


## PARA FAZER O SEU DEPLOY NÃO ESQUEÇA DE USAR O COMANDO PARA INSTALAR AS DEPENDÊNCIAS DO 'REQUIREMENTS.TXT'

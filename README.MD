# Instalando as depedencias 
        pip install -r .\requirements


# Docker

        docker compose up --build
        pytest --cov --cov-report=html

# CONFIGURAÇÕES A SERM FEITAS PARA CRIAR O PROJETO


        python3.7 -m venv <nome da venv>
        source env/bin/activate  # On Windows use `env\Scripts\activate`
        source venv/Scripts/activate

        pip install django==2.2.9
        python -m django startproject library .
        python -m django startapp cursos
        python manage.py makemigrations
        python manage.py migrate
        python manage.py createsuperuser
        python manage.py runserver
        pip install djangorestframework markdown django-filter
        python manage.py sqlflush
        pip install pymysql
        pip install django-enum-choices
        
        
# CONFIGURAÇÕES A SEREM FEITAS NO settings.py


            STATIC_URL = '/static/'
            STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
            MEDIA_URL = 'media/'
            MEDIA_ROOT = os.path.join(BASE_DIR,'media')

            INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',

                'django_filters',
                'rest_framework',

                'cursosTwo',
            ]
            REST_FRAMEWORK ={
                'DEFAULT_AUTHENTICATICON_CLASSES':(
                    'rest_framework.authentication.SessionAuthentication',
                ),
                'DEFAULT_PERMISSION_CLASSES':(
                    'rest_framework.persmissions.IsAuthenticatedOrReadOnly'
                )
            }
            

# LISTA DE MODULOS QE FOI USADO NO PROJETO


            pip freeze > requirements.txt


# JSON


        python manage.py shell  
        from rest_framework.renderers import JSONRenderer
        


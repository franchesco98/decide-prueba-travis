% prepara el repositorio para su despliegue. 
release: sh -c 'cp heroku_settings.py decide/decide/settings.py && cd decide && python manage.py migrate'
% especifica el comando para lanzar Decide
web: sh -c 'cd decide && gunicorn decide.wsgi --log-file -'

% prepara el repositorio para su despliegue. 
release: sh -c 'cd decide && cp heroku_settings.py decide/settings.py && python manage.py migrate'
% especifica el comando para lanzar Decide
web: sh -c 'cd decide && gunicorn decide.wsgi --log-file -'

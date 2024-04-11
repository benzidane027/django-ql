### this is django  project backend


to run project :

* docker compose up -d

how to add you a package :

* add package name to requirements.txt
  * docker compose build

to run migrations:

* docker compose exec api python manage.py migrate --noinput

to run fixtures: (deprecated)

docker compose exec api ./manage.py loaddata path/to/fixture/data.(yml or json)


to explore the db :

* docker-compose exec db psql --username={user} --dbname={db_name}

to run command inside container:

* docker compose exec api bash  -c "pip freeze"
  
to run test inside container:

* docker compose exec api ./manage.py test

django superuser:
  command: docker compose exec api bash -c "./manage.py createsuperuser "
  user : root
  email: <root@root.dz>
  pass : root

for generate ssl use the command:
    * openssl req -x509 -nodes -days 1000 -newkey rsa:2048 -keyout key.key -out cert.crt

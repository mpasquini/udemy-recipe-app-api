# udemy-recipe-app-api [![Build Status](https://travis-ci.org/mpasquini/udemy-recipe-app-api.svg?branch=development)](https://travis-ci.org/mpasquini/udemy-recipe-app-api)
Udemy course, recipe-app-api source code

complete solution: 
https://github.com/LondonAppDeveloper/recipe-app-api/tree/master/app/core



sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose


docker build .
docker-compose build
docker-compose run app sh -c "django-admin.py startproject app ."

# configure travis-ci
https://travis-ci.org

create .travis.yml
and add flake8 to requirements.txt

create .flake8 conf file under /app


# create new core django app  
docker-compose run app sh -c "python manage.py startapp core"

## custom user
create test to test user add with mail

create UserManager from BaseUserManager to create customized user

create User model that use UserManager ans set email as usernamefield
update settings.py to set AUTH_USER_MODEL = 'core.User'

make migrations
docker-compose run app sh -c "python manage.py makemigrations core" 

test it:
docker-compose run app sh -c "python manage.py test && flake8"



## custom admin
create tests test_admin.py
note: check django.test.Client documentation
note: check django.urls.reverse doc

testing user page change: 
-> test_user_change_page 
added "fieldsets" in admin.py

-> test_create_user_page
can create an user page?
added "add_fieldsets" in admin.py

# adding postgres
## docker compose
added: 
    envirounment:
      - DB_HOST=db
      - DB_NAME=app
      - DB_USER=postgres
      - DB_PASS=password
      #  - PGPASSFILE=.pgpass
    depends_on:
      - db

  db:
    image: postgres:10-alpine
    enviroument:
      - POSTGRES_DB=app
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
      

## first run, add wait for db command
-> app/core/management/commands, look for Django doc 
-> docker-compose up
note: cannot see full log output after migrations info message, 
app seems to work..., really ...???


## add superuser:
docker-compose run app sh -c "python manage.py createsuperuser"
--> 127.0.0.1:8000/admin to login 
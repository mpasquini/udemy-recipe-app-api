# udemy-recipe-app-api [![Build Status](https://travis-ci.org/mpasquini/udemy-recipe-app-api.svg?branch=development)](https://travis-ci.org/mpasquini/udemy-recipe-app-api)  
[link to tavis-ci](https://travis-ci.org/mpasquini/udemy-recipe-app-api)  

Coverage Report Status:  
```coverage
Name                  Stmts   Miss Branch BrPart     Cover   Missing
--------------------------------------------------------------------
user/serializers.py      29      0      4      1    96.97%   28->32
--------------------------------------------------------------------
TOTAL                   123      0      8      1    99.24%

15 files skipped due to complete coverage.
```


Udemy course, recipe-app-api source code  

[complete solution on LondonAppDeveloper](https://github.com/LondonAppDeveloper/recipe-app-api/tree/master/app/core)  

docker-compose 1.24.0 version:  
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose   
```  

```
docker build .  
docker-compose build  
docker-compose run -rm app sh -c "django-admin.py startproject app ."  
```

sometime is useful to free some docker unused space 
```bash    
docker system prune 
```  

# configure travis-ci
https://travis-ci.org

create .travis.yml
and add flake8 to requirements.txt

create .flake8 conf file under /app


# create new core django app  
```
docker-compose run app sh -c "python manage.py startapp core"
```

## custom user
create test to test user add with mail  

create UserManager from BaseUserManager to create customized user  

create User model that use UserManager ans set email as usernamefield  
update settings.py to set AUTH_USER_MODEL = 'core.User'  

make migrations:
```
docker-compose run app sh -c "python manage.py makemigrations core"   
```
test it:
```
docker-compose run app sh -c "python manage.py test && flake8"  
```


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
```docker-compose
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
```      

## first run, add wait for db command  
-> app/core/management/commands, look for Django doc   
```
docker-compose up    
```
note: cannot see full log output after migrations info message,     
app seems to work..., really ...???  


## add superuser:  
```bash
docker-compose run app sh -c "python manage.py createsuperuser"    
```
--> 127.0.0.1:8000/admin to login   

## create user rest api
introducing rest_framework.   
data are serialized in json, read and write  
user is a separate app  

```
docker-compose run --rm app sh -c "python manage.py startapp user"    
```
using path and include from django.urls, the requests are passed to proper app  

```
docker-compose run --rm app sh -c "python manage.py test && flake8"  

docker-compose run --rm app sh -c "coverage run manage.py test && flake8 && coverage report > /coverage/coverage_report.txt && coverage html "  
```



## temporary token for future api requests


## create used management


## recepie  app

```bash
docker-compose run --rm app sh -c "python manage.py startapp recipe"
```


##Tags - lecture49
add Tag model test amd model
```
docker-compose run app sh -c "python manage.py makemigrations"   
```
##Tags - lecture50
add tag test

##Tags - lecture51
add tag Selializer and create
insert, delele, update are inherithed by mixin class, 
oveloaded for the perform_create function only to make sure the tag is related to the authenticated user

## Ingredients - Lecture 53
add Ingredients model test amd model, same as Tag
```
docker-compose run app sh -c "python manage.py makemigrations core"    
```



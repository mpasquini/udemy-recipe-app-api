# udemy-recipe-app-api
Udemy course, recipe-app-api source code



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
docker-compose run app sh -c "python manage.py test"






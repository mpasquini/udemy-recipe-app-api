#####Original:  
  [udemy.com/django-python-advanced](https://garmin.udemy.com/django-python-advanced/learn/v4/content)  

###Section: 1  
Introduction

#####1 -  Welcome to Build a Backend API with Django REST Framework - Advanced 

#####2 -  Intro to the course 

  [Finished project on GitHub](https://github.com/LondonAppDeveloper/recipe-app-api)  

#####3 -  Course structure 
#####4 -  How to get the most out of this course 
#####5 -  How to get help 

        How to ask questions on Stack Overflow (and get answers!)

###Section: 2 - Technologies used in this course

#####6 -  Python 
    
  [Python](https://www.python.org/)  

#####7 -  Django 
  
  [Django](https://www.djangoproject.com/)  
#####8 -  Django REST Framework 
  
  [Django REST Framework](https://www.django-rest-framework.org/)  
#####9 -  Docker 
  
  [Docker](https://www.docker.com/)  
#####10 -  Travis-CI 
  
  [Travis-CI](https://travis-ci.org/)  
#####11 -  Postgres 
  
  [PostgreSQL](https://www.postgresql.org/)    

#####12 -  What is test driven development? 

###Section: 3 - Installation and setup
###Section: 4 - Create new project

#####15 - Setup new GitHub project 

  [GitHub](https://github.com/)  
  [Connecting to GitHub with SSH](https://help.github.com/articles/connecting-to-github-with-ssh/)  

#####16 -  Add Dockerfile 

  [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)  
  [Docker Hub](https://hub.docker.com/)  
  [Python Package Index PyPi](https://pypi.org/)  
  CODE: Dockerfile    
  CODE: requirements.txt    

#####17 -  Configure Docker Compose 

  [Docker Compose](https://docs.docker.com/compose/)  
  CODE: docker-compose.yml    

#####18 -  Create Django project 

  [Django startproject docs](https://docs.djangoproject.com/en/2.1/ref/django-admin/#startproject)  
  [Docker compose run command reference](https://docs.docker.com/compose/reference/run/)  

###Section: 5 - Setup automation

#####19 -  Enable Travis-CI for project 

  [Travis-CI](https://travis-ci.org/)  

#####20 -  Create Travis-CI configuration file 

  [Travis-CI Tutorial](https://docs.travis-ci.com/user/tutorial/)  
  [Python Flake8](http://flake8.pycqa.org/en/latest/)  
  CODE: .travis.yml    
  CODE: requirements.txt    
  CODE: .flake8    

Quiz 1: Travis-CI
###Section: 6 - Introduction to test driven development (TDD)

#####21 -  Writing a simple unit test 

  [Django unit tests](https://docs.djangoproject.com/en/2.1/internals/contributing/writing-code/unit-tests/)  
  CODE: calc.py      
  CODE: tests.py      

#####22 -  Writing a unit test with TDD 

  [unittest library assert statements](https://docs.python.org/3/library/unittest.html#assert-methods)  
  [Django manage.py test](https://docs.djangoproject.com/en/2.1/ref/django-admin/#test)  
  CODE: tests.py      
  CODE: tests.py (before)      
  CODE: tests.py (after)      

Quiz 2: Django Unit Tests
###Section: 7 - Configure Django custom user model

#####23 -  Create core app 

  [Django manage.py startapp docs](https://docs.djangoproject.com/en/2.1/ref/django-admin/#startapp)  
  [Django settings INSTALLED_APPS](https://docs.djangoproject.com/en/2.1/ref/settings/#installed-apps)  

#####24 -  Add tests for custom user model 

  [Substituting a custom User model in Django](https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#substituting-a-custom-user-model)  
  [get_user_model() docs](https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#django.contrib.auth.get_user_model)  
  [check_password() docs](https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser.check_password)  
  CODE: test_models.py    

#####25 - Implement custom user model 

  [AbstractBaseUser docs](https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser)  
  [BaseUserManager docs](https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager)  
  [PermissionsMixin docs](https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#django.contrib.auth.models.PermissionsMixin)  
  CODE: models.py    
  CODE: settings.py    

#####26 - Normalize email addresses 

  [Django docs for normalize_email function](https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager.normalize_email)  
  CODE: test_models.py    
  CODE: models.py    

#####27 - Add validation for email field 

  CODE: test_models.py    
  CODE: models.py    

#####28 - Add support for creating superusers 

  [Django manage.py createsuperuser docs](https://docs.djangoproject.com/en/2.1/ref/django-admin/#createsuperuser)  
  CODE: test_models.py    
  CODE: models.py    

Quiz 3: Django custom user model
###Section: 8 - Setup Django admin

#####29 - Add tests for listing users in Django admin 

  [Django admin docs](https://docs.djangoproject.com/en/2.1/ref/contrib/admin/)  
  CODE: test_admin.py    

#####30 - Modify Django admin to list our custom user model 

CODE: admin.py  

#####31 - Modify Django admin to support changing user model 

  [Django admin fieldsets](https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets)  
  CODE: test_admin.py    
  CODE: admin.py    

#####32 - Modify Django admin to support creating users 

  CODE: test_admin.py    
  CODE: admin.py    

###Section: 9 - Setting up database

#####33 - Add postgres to docker compose 

  [Environment variables in Docker Compose](https://docs.docker.com/compose/environment-variables/)  
  [Postgres on Docker Hub](https://hub.docker.com/_/postgres/)  
  [Docker Compose depends_on](https://docs.docker.com/compose/compose-file/#depends_on)  
  CODE: docker-compose.yml  

#####34 - Add postgres support to Dockerfile 

  [psycopg2 on PyPi](https://pypi.org/project/psycopg2/)  
  [Alpine Linux package management](https://pypi.org/project/psycopg2/)  
  CODE: requirements.txt  
  CODE: Dockerfile  

#####35 - Configure database in Django 

  [Django DATABASES setting](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-DATABASES)  
  [Django PostgreSQL database notes](https://docs.djangoproject.com/en/2.1/ref/databases/#postgresql-notes)  
  [Python os.envion](https://docs.python.org/3/library/os.html#os.environ)  
  CODE: settings.py    

###Section: 10 - Waiting for postgres to start

#####36 - Mocking with unittests 

#####37 - Add tests for wait_for_db command 

    Writing custom django-admin commands
    Django management call_command
    GitHub Django code for connection handler
    Stack Overflow question for unit testing wait_for_db command
  CODE: test_commands.py    

#####38 - Add wait_for_db command 

    Writing custom django-admin commands
  CODE: wait_for_db.py    

#####39 - Make docker compose wait for db 

  CODE: docker-compose.yml  

#####40 - Test in browser 
Quiz 4: Mocking
###Section: 11 - Create user management endpoints

#####41 - Create users app 

#####42 - Add tests for create user API 

  CODE: test_user_api.py    
    get_user_model official documentation

#####43 - Add create user API 

    Django REST Framework ModelSerializer docs
    Django REST Framework CreateAPIView docs
  CODE: serializers.py    
  CODE: views.py    
  CODE: urls.py    

#####44 - Add tests for creating a new token 

  CODE: test_user_api.py    

#####45 - Add create token API 

    Django REST Framework ObtainAuthToken
    GitHub Django REST Framework AuthTokenSerializer
  CODE: serializers.py    
  CODE: views.py    
  CODE: urls.py    

#####46 - Add tests for manage user endpoint 

  CODE: test_user_api.py    

#####47 - Add manage user endpoint 

        ModHeader
        Django REST Framework RetrieveUpdateAPIView
  CODE: views.py    
  CODE: serializers.py    
  CODE: urls.py    

###Section: 12 - Create tags endpoint

#####48 - Create recipe app 

#####49 - Add tag model 

  [Django model str](https://docs.djangoproject.com/en/2.1/ref/models/instances/#django.db.models.Model.__str__)  
  [Django Admin Register](https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin)  
  [Django ForeignKey docs](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey)  
  [Django ForeignKey on_delete docs](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete)  
  CODE: test_models.py    
  CODE: models.py    
  CODE: admin.py    

#####50 - Add tests for listing tags 

  [HTTP Status Codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)  
  CODE: test_tags_api.py    

#####51 - Add feature to list tags 

  [Django REST Framework ModelSerializer](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)  
  [Django REST Framework GenericViewSet](https://www.django-rest-framework.org/api-guide/viewsets/#genericviewset)  
  [Django REST Framework Example of using GenericViewSet](https://www.django-rest-framework.org/api-guide/viewsets/#example_3)  
  CODE: serializers.py    
  CODE: views.py    
  CODE: recipes/urls.py    
  CODE: app/urls.py    
  CODE: views.py    


#####52 - Add create tags feature 

  CODE: test_tags_api.py    
  CODE: views.py    

###Section: 13 - Create ingredients endpoint

#####53 - Add ingredient model 

  CODE: test_models.py    
  CODE: models.py    
  CODE: admin.py    

#####54 - Add tests for listing ingredients 

  CODE: test_ingredients_api.py    

#####55 - Implement feature for list ingredients 

  CODE: serializers.py    
  CODE: views.py    
  CODE: urls.py    

#####56 - Implement feature for creating ingredients 

  CODE: test_ingredients_api.py    
  CODE: views.py    

#####57 - Re-factor tags and ingredients viewsets 

  CODE: views.py    

###Section: 14 - Create recipe endpoint

#####58 - Add recipe model 

    Django ManyToManyField
  CODE: test_models.py    
  CODE: models.py    
  CODE: admin.py    

#####59 - Add tests for listing recipes 

  CODE: test_recipe_api.py    

#####60 - Implement feature for listing recipes 

    Django REST Framework PrimaryKeyRelatedField
  CODE: serializers.py    
  CODE: views.py    
  CODE: urls.py    

#####61 - Add tests for retrieving recipe detail 

  CODE: test_recipe_api.py    

#####62 - Implement feature for retrieving recipe detail 

    Django REST Framework get_serializer_class()
  CODE: serializers.py    
  CODE: views.py    

#####63 - Add tests for creating recipes 

    Python getattr docs
  CODE: test_recipe_api.py    

#####64 - Implement feature for creating recipes 

    Django REST Framework assigning model items ot users
  CODE: views.py    

#####65 - Add tests for updating recipes 

  CODE: test_recipe_api.py    

###Section: 15 - Add upload image endpoint

#####66 - Add Pillow requirement 

    Django ImageField
  CODE: requirements.txt  
  CODE: Dockerfile  
  CODE: settings.py    
  CODE: urls.py    
    Pillow

#####67 - Modify recipe model 

    Python uuid4
    Python FileField upload_to
  CODE: test_models.py    
  CODE: models.py    

#####68 - Add tests for uploading image to recipe 

    Python NamedTemporaryFile
  CODE: test_recipe_api.py    

#####69 - Add feature to upload image 

        Django REST Framework adding action to viewset
  CODE: serializers.py    
  CODE: views.py    

###Section: 16 - Add filtering

#####70 - Add tests for filtering recipes 

  CODE: test_recipe_api.py    

#####71 - Implement feature to filter recipes 

  CODE: views.py    

#####72 - Add tests for filtering tags and ingredients 

  CODE: test_tags_api.py    
  CODE: test_ingredients_api.py    

#####73 - Implement feature for filtering tags and ingredients 

  CODE: views.py    

###Section: 17 - Summary
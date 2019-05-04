pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_VERSION='1.24.0'
    }
    stages {
        stage('before_install') {
            steps {
              sudo rm /usr/local/bin/docker-compose
              curl -L https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-compose-`uname -s`-`uname -m` > docker-compose
              chmod +x docker-compose
              sudo mv docker-compose /usr/local/bin
            }

        stage('before_scripts') {
            steps {
                pip install docker-compose
            }
        }

        stage('test')
            steps {
                docker-compose run app sh -c "python manage.py test && flake8"
            }
        }
    }
}
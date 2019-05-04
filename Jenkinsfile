pipeline {
    agent any
    stages {

        stage('before_install') {
            environment {
                DOCKER_COMPOSE_VERSION='1.24.0'
            }
            steps {
                sh """
                  rm /usr/local/bin/docker-compose
                  curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > docker-compose
                  chmod +x docker-compose
                  mv docker-compose /usr/local/bin
                """
            }
        }

        stage('before_scripts') {
            steps {
                sh """
                pip install docker-compose
                """
            }
        }

        stage('test'){
            steps {
                sh """
                docker-compose run app sh -c 'python manage.py test && flake8'
                """
            }
        }
    }
}
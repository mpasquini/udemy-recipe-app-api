pipeline {
    agent { label 'jenkins-docker-109' }
    stages {

        stage('before_install') {
            environment {
                DOCKER_COMPOSE_VERSION='1.24.0'
            }
            steps {
                sh """
                  sudo apt install -y python3 python3-pip
                  curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > docker-compose
                  chmod +x docker-compose
                  sudo mv docker-compose /usr/local/bin
                """
            }
        }

        stage('before_scripts') {
            steps {
                sh """
                sudo pip3 install docker-compose
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
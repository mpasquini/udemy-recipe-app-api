pipeline {
    agent { label 'jenkins-docker-109' }
    stages {

        stage('before_install') {
            environment {
                DOCKER_COMPOSE_VERSION='1.24.0'
            }
            steps {
                sh """
                  sudo apt-get update
                  sudo apt-get upgrade
                  sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev  libncursesw5-dev xz-utils tk-dev
                  wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz
                  tar xvf Python-3.6.6.tgz
                  cd Python-3.6.6
                  ./configure --enable-optimizations --with-ensurepip=install
                  make -j 8
                  sudo make altinstall

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
pipeline {
    agent any

    stages {
        stage('Pobranie kodu') {
            steps {
                checkout scm
            }
        }

        stage('Budowanie') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest requests
                '''
            }
        }

        stage('Testy jednostkowe') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -v
                '''
            }
        }

        stage('Wdrożenie testowe') {
            steps {
                echo 'Wdrażanie aplikacji na środowisko testowe...'
                sh 'echo "Deployment zakończony sukcesem!"'
            }
        }
    }
}
pipeline {
    agent any
    
    stages {
        stage('Pobranie kodu') {
            steps {
                // Pobiera kod z GitHuba
                checkout scm
            }
        }
        
        stage('Budowanie') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Testy jednostkowe') {
            steps {
                sh 'pytest -v'
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
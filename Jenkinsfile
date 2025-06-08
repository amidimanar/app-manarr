pipeline {
    agent any

    stages {
        stage('Cloner le dépôt') {
            steps {
                echo 'Clonage automatique par Jenkins depuis GitHub...'
            }
        }

        stage('Installer les dépendances') {
            steps {
                echo 'Installation des dépendances...'
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Exécuter les tests') {
            steps {
                echo 'Lancement des tests Django...'
                sh './venv/bin/python manage.py test'
            }
        }
    }

    post {
        always {
            echo 'Pipeline terminé.'
        }
        failure {
            echo 'Le pipeline a échoué ❌'
        }
        success {
            echo 'Le pipeline a réussi ✅'
        }
    }
}

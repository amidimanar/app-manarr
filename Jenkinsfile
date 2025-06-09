pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root:root'  // Pour exécuter en root (facilite l'install)
        }
    }
    environment {
        PYTHONUNBUFFERED = '1'  // Pour que les logs s'affichent directement
    }
    stages {
        stage('Install linters') {
            steps {
                sh '''
                    pip install --upgrade pip
                    pip install flake8 pylint bandit
                '''
            }
        }
        stage('Run flake8') {
            steps {
                sh 'flake8 backend/agrovera_microservices'
            }
        }
        stage('Run pylint') {
            steps {
                sh 'pylint backend/agrovera_microservices'
            }
        }
        stage('Run bandit') {
            steps {
                sh 'bandit -r backend/agrovera_microservices'
            }
        }
    
        stage('Build Docker Images') {
            steps {
                script {
                    def base = 'backend/agrovera_microservices'
                    def services = ['auth_service', 'user_service', 'payment_service', 'contact_service']
                    for (svc in services) {
                        sh "docker build -t ${DOCKER_REGISTRY}/${svc}:latest ${base}/${svc}"
                    }
                    sh "docker build -t ${DOCKER_REGISTRY}/frontend:latest ./frontend"
                }
            }
        }

        stage('Push to Registry') {
            steps {
                script {
                    def services = ['auth_service', 'user_service', 'payment_service', 'contact_service', 'frontend']
                    for (svc in services) {
                        sh "docker push ${DOCKER_REGISTRY}/${svc}:latest"
                    }
                }
            }
        }
    }
}

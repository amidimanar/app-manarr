pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "localhost:5000"
        SONAR_URL = "http://localhost:9000"
        SONAR_TOKEN = credentials('sonar-token') // à configurer dans Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/amidimanar/app-manarr.git', branch: 'main'
            }
        }

        stage('Analyse SonarQube') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner -Dsonar.projectKey=app-manarr -Dsonar.sources=backend -Dsonar.host.url=$SONAR_URL -Dsonar.login=$SONAR_TOKEN'
                }
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

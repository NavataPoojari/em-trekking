pipeline {
    agent any

    environment {
        DOCKER_USERNAME = "navatha24"
        BACKEND_IMAGE   = "trekky-backend"
        FRONTEND_IMAGE  = "trekky-frontend"
        K8S_NAMESPACE   = "default"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                bat "docker build -t %DOCKER_USERNAME%/%BACKEND_IMAGE%:%BUILD_NUMBER% backend"
                bat "docker build -t %DOCKER_USERNAME%/%FRONTEND_IMAGE%:%BUILD_NUMBER% frontend"
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DH_USER',
                    passwordVariable: 'DH_PASS'
                )]) {
                    bat "docker login -u %DH_USER% -p %DH_PASS%"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat "docker push %DOCKER_USERNAME%/%BACKEND_IMAGE%:%BUILD_NUMBER%"
                bat "docker push %DOCKER_USERNAME%/%FRONTEND_IMAGE%:%BUILD_NUMBER%"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat "kubectl apply -f k8s/backend-deployment.yaml"
                bat "kubectl apply -f k8s/backend-service.yaml"
                bat "kubectl apply -f k8s/frontend-deployment.yaml"
                bat "kubectl apply -f k8s/frontend-service.yaml"
            }
        }
    }
}

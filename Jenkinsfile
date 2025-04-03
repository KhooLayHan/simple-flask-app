pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/KhooLayHan/simple-flask-app.git'
            }
        }

        stage('Test') {
            steps {
                sh 'python -m pytest tests/'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("yourdockerhub/flask-app:${env.BUILD_ID}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Deploy Locally') {  // Deploy to Docker in WSL
            steps {
                sh """
                    docker stop flask-app || true
                    docker rm flask-app || true
                    docker run -d -p 5000:5000 --name flask-app yourdockerhub/flask-app:${env.BUILD_ID}
                """
            }
        }
    }
}
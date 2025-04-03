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
                sh '''
                    pip3 install -r requirements.txt
                    python3 -m pytest tests/
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("vincentkhoo01/simple-flask-app:${env.BUILD_ID}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dckr_pat_nsnEw6ug2pe-npGUoBcUwMCx45w') {
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
                    docker run -d -p 5000:5000 --name flask-app vincentkhoo01/simple-flask-app:${env.BUILD_ID}
                """
            }
        }
    }
}
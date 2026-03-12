pipeline {
    agent {
        docker {
            image 'golang:1.26.1-alpine3.23'
            args '-v /var/run/docker.sock:/var/run/docker.sock'  // Mount socket
        }
    }
    environment {
        DOCKER_HOST = 'tcp://socat-container:2375'
    }
    stages {
        stage('build') {
            steps {
                sh 'go version'
                sh 'docker version'  // Test Docker access
                sh 'docker ps'        // List containers
            }
        }
    }
}

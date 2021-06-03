pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh "chmod +x -R ${env.WORKSPACE}"
                sh "./jenkins/test.sh"
            }
        }
        stage('Build images') {
            steps {
                sh "./jenkins/build.sh"
            }
        }
    }
}
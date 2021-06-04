pipeline {
    agent any
    environment{
        DOCKER_LOGIN = credentials("DOCKER_LOGIN")
    }
    stages {
        stage('Test') {
            steps {
                sh "chmod +x -R ${env.WORKSPACE}"
                sh "./jenkins/test.sh"
            }
        }
        stage('Set-Up Docker'){
            steps{
                sh "./jenkins/setup-docker.sh"
            }
        }
        stage('Build images') {
            steps {
                sh "./jenkins/build.sh"
            }
        }
        stage('Push images') {
            steps {
                sh "./jenkins/push.sh"
            }
        }
        stage('Set-up Ansible') { 
            steps {
                sh "./jenkins/ansible.sh"
            }
        }
        stage('Configuration') {
            steps {
                sh 'ansible-playbook -i ./ansible/inventory.yaml ./ansible/playbook.yaml'
            }
        }
    }
}
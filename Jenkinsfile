pipeline {
    agent any

    stages {
        stage('Build image') {
            steps {
                sh 'echo "Building Docker image..."'
                sh 'docker build -t ttl.sh/jorgeajimenezl-app .'
                sh 'docker images'
            }
        }
        stage('Push image') {
            steps {
                sh 'echo "Pushing Docker image..."'
                sh 'docker push ttl.sh/jorgeajimenezl-app'
            }
        }
        // stage('Deploy') {
        //     environment {
        //         ANSIBLE_HOST_KEY_CHECKING = 'false'
        //     }
        //     steps {
        //         sh 'echo "Deploying..."'
        //         ansiblePlaybook credentialsId: 'mykey2',
        //                         inventory: 'hosts.ini',
        //                         playbook: 'playbook.yml'
        //     }
        // }
    }
}

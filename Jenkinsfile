pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'building'
            }
        }
        stage('test') {
            steps {
                echo 'testing'
                pwd
                ls
            }
        }
    }
    post {
        always {
        //ded
        }
        sucess {
        //ce
        }
        failure {
        //efe
        }
    }
}

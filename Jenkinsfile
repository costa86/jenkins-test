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
                echo BRANCH_NAME
            }
        }
    }
}

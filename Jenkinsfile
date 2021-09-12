pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'building'
            }
        }
        stage('test') {
            when {
                expression {
                    BRANCH_NAME == 'master'
                }
            }
            steps {
                echo "testing on $BRANCH_NAME"
            }
        }
    }
}

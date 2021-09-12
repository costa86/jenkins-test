pipeline {
    agent any
    environment {
        NEW_VERSION = '1.2.0'
        SERVER_CREDENTIALS = credentials('mock-user')
    }
    stages {
        stage('build') {
            steps {
                echo 'building'
                echo "building ${NEW_VERSION}"
            }
        }
        stage('test') {
            when {
                expression {
                    BRANCH_NAME == 'master'
                }
            }
            steps {
                echo "testing on ${BRANCH_NAME}"
            }
        }
    }
}

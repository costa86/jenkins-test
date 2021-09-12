pipeline {
    agent any
    parameters {
        choice(name:'MODE', choices:['dev', 'prod'], description:'environment')
    }
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
                    parameters.MODE == "dev"
                }
            }
            steps {
                echo "testing on ${BRANCH_NAME}"
            }
        }
    }
}

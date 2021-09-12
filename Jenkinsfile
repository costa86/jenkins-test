def gv

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
        stage("init"){
            steps{
                script {
                    gv = load "script.groovy"
                }
            }
        }
        stage('build') {
            steps {
                echo "building ${NEW_VERSION}"
                script {
                    gv.buildApp()
                }
            }
        }
        stage('test') {
            when {
                expression {
                    BRANCH_NAME == 'master' && params.MODE == 'dev'
                }
            }
            steps {
                echo "testing on ${BRANCH_NAME}"
                echo $USER
            }
        }
    }
}

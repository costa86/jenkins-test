def gv

pipeline {
    agent any
    environment {
        SSH = credentials('ssh')
    }

    parameters {
        choice(name:'MODE', choices:['dev', 'prod'], description:'environment')
        booleanParam(name:'runTests', defaultValue:true, description:'Run tests?')
    }

    stages {
        stage('init') {
            steps {
                script {
                    gv = load 'script.groovy'
                }
            }
        }
        stage('build') {
            steps {
                echo 'building ola'
                echo "Running on ${params.MODE}"
                sh 'whoami'
                sh 'ls'
                sh('scp -o StrictHostKeyChecking=no app.py -i $SSH costa@64.90.185.208:')
            }
        }
        stage('test') {
            when {
                expression {
                    params.runTests
                }
            }
            steps {
                script {
                    gv.testApp()
                }
            }
        }
    }
}

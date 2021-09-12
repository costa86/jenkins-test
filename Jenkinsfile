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
                sh('ssh -o StrictHostKeyChecking=no -i $SSH costa@164.90.185.208 whoami')
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


pipeline {
    agent any
    parameters {
        choice(name:'MODE', choices:['dev', 'prod'], description:'environment')
        booleanParam(name:'runTests', defaultValue:true, description:'Run tests?')
    }

    stages {
        stage('build') {
            steps {
                echo 'building ola'
                echo "Running on ${params.MODE}"
            }
        }
        stage('test') {
            when {
                expression {
                    params.runTests
                }
                steps {
                    echo 'running tests'
                }
            }
        }
    }
}


pipeline {
    agent any
    parameters {
        choice(name:'MODE', choices:['dev', 'prod'], description:'environment')
    }

    stages {
        stage('build') {
            steps {
                echo 'building ola'
                echo "Running on ${params.MODE}"
            }
        }
    }
}

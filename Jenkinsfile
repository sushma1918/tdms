pipeline {
    agent any
 
    stages {
        stage('Hello') {
            steps {
                sh'''
                echo "hello"
                 curl -v -u 'B0268061:4^Dsheod' --upload-file Path http://nexus.airtelworld.in:8081/repository/Darts-devops/tdms_datasets/$name
                '''
            }
        }
        
        
        
    }
}

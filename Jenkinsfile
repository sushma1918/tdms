pipeline {
    agent any
 
    stages {
        stage('Hello') {
            steps {
                sh'''
                 curl  -u  'B0268061:4^Dsheod'  -o $Select_excel_file http://nexus.airtelworld.in:8081/repository/Darts-devops/tdms_datasets/$Select_excel_file
                 source  /Users/b0268061/Desktop/tdms/tdms_env/bin/activate && python /Users/b0268061/Desktop/tdms/generate_data.py
                 rm $Select_excel_file 
 
                '''
            }
        }
        
        
        
    }
}

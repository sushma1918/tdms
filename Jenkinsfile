pipeline {
    agent{
        label "dev_236_11"
    }

    stages {
        stage('Download file form nexus ') {
            
            steps {
                sh '''
                ssh 10.240.0.167 "curl  -u  B0268061:4^Dsheod  --url http://nexus.airtelworld.in:8081/repository/Darts-devops/tdms_data_sets/UPCDeatils.xlsx -o /data/tdms/${Select_excel_file}"
                '''
            }
        }
        stage('Execute script ') {
            steps {
                sh '''

                ssh 10.240.0.167 "source /data/tdms/env/bin/activate && python /data/tdms/generate_data.py ${Select_excel_file} ${File_name} ${Number_of_recode} ${Action}"
                '''
            }
        }
        
    }
}


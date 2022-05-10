
pipeline {
   agent any
   
   stages {
       
         stage('GET CSV FILE') {
             steps {
                 script {
                   
                        def file_name = input(id: 'inputTextbox', message: 'Please Enter file name', parameters: [[$class: 'TextParameterDefinition', description: 'Please enter file name that you want to upload ',name: 'input']])
                            echo ("FILE Name : ${file_name}")
                          
                        def file_path = input message: 'Upload file', parameters: [file(name: file_name, description: 'Upload only CSV file')]
                          echo ("CSV FILE PATH IS : ${file_path}")
                       sh'''
                       mv ${file_path} ${file_name}
                       '''
                          
                        url = 'http://nexus.airtelworld.in:8081/service/rest/v1/components?repository=Darts-devops'
                        def query = ["curl", "-u", "B0268061:4^Dsheod",  "-X", "POST", "--url", "http://nexus.airtelworld.in:8081/service/rest/v1/components?repository=Darts-devops",  "-F",  "raw.directory=tdms_data_sets",  "-F",  "raw.asset1=${file_name}", "-F", "raw.asset1.filename=${file_name}" ]
                        query.execute().text
                        echo 'new dataset stored '
                 }
              }
             
         }
         
   }
    
}
       


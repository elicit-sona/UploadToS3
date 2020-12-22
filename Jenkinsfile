pipeline{
	agent any

	
	stages{
		stage("zip source code"){
			steps{
			
			sh 'echo "ziping your source code............"'
			sh 'zip -r source_code.zip * -x Jenkinsfile'
                        sh 'ls'
			}
		}
                
                stage("upload artifacts to S3"){
			steps{
			 withAWS(region:'us-east-1',credentials:'awscreds') {

                                

                                // Upload files from working directory 'dist' in your project workspace
                                s3Upload(bucket:"bu-lambda", file:"source_code.zip");
                        }
			}	
	        }
	
       }
}


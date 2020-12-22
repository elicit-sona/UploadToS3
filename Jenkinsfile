pipeline{
	agent any

	
	stages{
		stage("zip source code"){
			steps{
			
			sh 'echo "ziping your source code............"'
			sh 'zip -r source_code.zip * -x JenkinsFile'
                        sh 'ls'
			}
		}
                
                stage("upload artifacts to S3"){
			steps{
			 withAWS(region:'us-east-1',credentials:'awscreds') {

                                def identity=awsIdentity();//Log AWS credentials

                                // Upload files from working directory 'dist' in your project workspace
                                s3Upload(bucket:"bu-lambda", sourceFile:"**/source_code.zip");
                        }
			}	
	        }
	
       }
}


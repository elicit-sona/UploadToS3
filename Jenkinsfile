pipeline{
	agent any
	
	parameters{
		string(name: 'BUCKET_REGION', defaultValue: 'us-east-1', description: 'specify the region where bucket resides')
	}
	
	stages{
		stage("zip source code"){
			steps{
			sh 'echo "$BUCKET_REGION"'
			sh 'echo "ziping your source code............"'
			sh 'zip -r source_code.zip * -x Jenkinsfile '
                        sh 'ls'
			}
		}
                
                stage("upload artifacts to S3"){
			steps{
			 withAWS(region: env.BUCKET_REGION, credentials:'awscreds') {

                                

                                // Upload files from working directory 'dist' in your project workspace
                                s3Upload(bucket:"bu-lambda", file:"source_code.zip", path:"JenkinsArtifacts/");
                        }
			}	
	        }
	
       }
}


pipeline{
	agent any
	
	parameters{
		string(name: 'BUCKET_REGION', defaultValue: 'us-east-1', description: 'specify the region where bucket resides')
		string(name: 'BUCKET_NAME', defaultValue: 'bu-lambda', description: 'specify the bucket name')
		string(name: 'GIT_URL', defaultValue: 'https://github.com/elicit-sona/UploadToS3.git', description: 'specify git url')
		string(name: 'BRANCH', defaultValue: 'master', description: 'enter branch name')
		string(name: 'GIT_CREDENTIALS_ID', defaultValue: 'gitcreds', description: 'specify which credentials id to be used')
		
	}
	
	stages{
		 stage("Checkout code") {
			 steps{
				 git branch: BRANCH,
					 credentialsId: GIT_CREDENTIALS_ID,
					 url: GIT_URL

				 sh 'ls -lart ./*'
   			}
  		}
		stage("zip source code"){
			steps{
			sh 'echo "ziping your source code............"'
			sh 'zip -r source_code.zip * --exclude Jenkinsfile'
			}
		}
                
                stage("upload artifacts to S3"){
			steps{
			sh 'echo "uploading artifacts to S3 Bucket $BUCKET_NAME............."'
			withAWS(region: env.BUCKET_REGION, credentials:'awscreds') {
                                // Upload files to S3 bucket
                                s3Upload(bucket: env.BUCKET_NAME, file:"source_code.zip", path:"JenkinsArtifacts/");
                        }
			}	
	        }
	
       }
}


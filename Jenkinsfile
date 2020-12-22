pipeline{
	agent any

	
	stages{
		stage("zip source code"){
			steps{
			
			sh 'echo "ziping your source code............"'
			sh 'zip -r source_code.zip * -x JenkinsFile'
			}
		}	
	}
	
}


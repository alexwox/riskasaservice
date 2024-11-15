# riskasaservice





When making changes to the code, run the following commands:

To build and run the container:
bash docker buildx build --platform linux/amd64 -t <id>.dkr.ecr.eu-north-1.amazonaws.com/riskasaservice:latest --push .

Add subnet ports to allow traffic to the container from the VPC on AWS. 

Make sure the correct container is in ECR

Connect container to the Task Definition. 

Run task definition with cluster. 



# Problem Statement

Predicing Year of Marriage model deployment with Flask-AWS

# Steps for Model Building and  hosting local API
1. Data Preparation
2. Machine Learning Modelling
3. Model Evaluation
4. Export Trained Model
5. LOCAL REST API with Flask web-server 
6. Create a website for predicing marriage age calling REST API

# Steps for Deploying Public API to AWS EC2 server and launch website service 

1. Spin up an EC2 server
2. Configure EC2 with security group and private key
3. Install libraries and dependencies on the EC2 server
4. Move trained model and app.py flask files to EC2 (winscp)
5. Configure flaskapp.wsgi file and Apache vhost file
6. Restart apache webserver and Check API status
7. Launch a website with domain name and host webpage.

# FastAPI_Dashboard
This repository is for the AWS FastAPI dashboard

# Table of Contents
- [Project Objectives]
- [Project Overview/Features]
- [Architecture Diagram]
- [Prerequisites]
- [Project Steps]
- [Demo of completed project]
- [Contributors]

# Project Objectives
In this project I sought out to create a web app that monitors and retives the combined cost of all my running ec2 instances and s3 buckets. I deployed this web app on an ec2 instance that resides in a public facing subnet on a custom VPC.   

# Project Overview/Features
This project involves the use of several technologies such as Terraform for IaC(Infastructure-as-Code). AWS services such as ec2, s3, and VPC. Python libaries such as boto3(AWS SDK), FastAPI, and FastAPI templates such as Jinja2Templates. NGINX for the web app hosting. Lastly, I used Html to build the dashboard template for Jinja2. 

# Architecture Diagram
![FastAPI AWS DIagram (1)](https://github.com/Shaitown904/FastAPI_Dashboard/assets/155275814/da4034f3-54c7-4371-aad2-f93e8969f52f)
The Diagram represents a client making a http request to the ec2 instance hosting the web app.

# Prerequisites
Enable to do this project you must have the follwoing installed and configured:
- AWS account
- VS Code(or any code text editor of your choice)
- The latest version of Hashicorp Terraform
- The latest version of python3

# Project Steps
####Deploying the AWS infrastrucure Directions
1. Create a project folder
2. Open VS code and open a terminal window
3. Navigate to the project folder `cd /path/to/project_folder`
4. Run the command `git clone https://github.com/Shaitown904/FastAPI_Dashboard/` to clone repository files
5. Open Infra.tf and use your own AWS access keys for CLI
6. Edit the Infra.tf file to meet your needs
7. In the terminal, run `Terraform init` to initilaize Terraform
8. Next, run `Terraform plan` to check what resources will be built
9. Lastly, run `Terraform apply` to deploy the infrastructure

###Setting up the ec2 Instance
Once our infastructure is built, do the following:
1. Navigate to your aws console >> ec2 >> actions >> Network >> manage IP addresses
2. Toggle on Auto Assign IP addreses
   
https://github.com/Shaitown904/FastAPI_Dashboard/assets/155275814/11d12555-0e2c-4011-b60d-1884c7174d24

4. Now Navigate to connect Instance you can either choose ssh or ec2 Instance Connect
5. Once in the ec2 instance, we have to install and configure NGINX for our Ubuntu ec2 Instance
6. Run the command `sudo apt install -y python3` since python does not come with the instance
7. Next, run `sudo apt install -y python3 nginx` to install NGINX
8. Next, run the command `sudo vim /etc/nginx/sites-enabled/fastapi_nginx`(This will allow us to configure NGINX to run our app on the server by routing the local host traffic to the ec2 ip address.)
9. Next, in the vim editor type:
   server {
    listen 80;   
    server_name #place your ec2 public ip  address here;    
    location / {        
        proxy_pass http://127.0.0.1:8000;    
    }
}
10. Run `sudo service nginx restart`
11. Run the command `git clone https://github.com/Shaitown904/FastAPI_Dashboard/` to clone repository files to ec2 instance
12. Run `python3 -m venv .venv`
13. Run `source .venv/bin/activate`
14. Run `python3 -m pip install -r requirements.txt` ####Note if you skip the previous two steps you will get an error depending on which OS you are using
15. Run `python3 -m uvicorn dashboard:app`
16. Lastly, visit http://your_ec2_ip_address.com
   

# Demo of completed project
https://github.com/Shaitown904/FastAPI_Dashboard/assets/155275814/82b7976c-9d67-4ab8-a8a6-4ae612ca098a

# Contibuters
Shaitown904


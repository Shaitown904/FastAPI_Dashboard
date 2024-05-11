# FastAPI_Dashboard
This repository is for the AWS FastAPI dashboard

# Table of Contents
- [Project Objectives]
- [Project Overview/Features]
- [Architecture Diagram]
- [Prerequisites]
- [Getting Started]
- [Project Steps]
- [Demo of completed project]
- [Key Findings/Lessons Learned]
- [Contributors]

# Project Objectives
In this project I sought out to create a web app that monitors and retives the combined cost of all my running ec2 instances and s3 buckets. I deployed this web app on an ec2 instance that resides in a public facing subnet on a custom VPC.   

# Project Overview/Features
This project involves the use of several technologies such as Terraform for IaC(Infastructure-as-Code). AWS services such as ec2, s3, and VPC. Python libaries such as boto3(AWS SDK), FastAPI, and FastAPI templates such as Jinja2Templates. NGINX for the web app hosting. Lastly, I used Html to build the dashboard template for Jinja2. 

# Architecture Diagram
![FastAPI AWS DIagram (1)](https://github.com/Shaitown904/FastAPI_Dashboard/assets/155275814/da4034f3-54c7-4371-aad2-f93e8969f52f)
The Diagram represents a client making a http request to the ec2 instance hosting the web app.

# Demo of completed project
https://github.com/Shaitown904/FastAPI_Dashboard/assets/155275814/82b7976c-9d67-4ab8-a8a6-4ae612ca098a


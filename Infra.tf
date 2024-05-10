# Provider is AWS
provider "aws" {
  region     = "us-east-1"
  access_key = ""
  secret_key = ""
}

# Creating the VPC
resource "aws_vpc" "API_VPC" {
  cidr_block = "10.0.0.0/16"
}

# Create the subnet for VPC
resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.API_VPC.id
  cidr_block = "10.0.1.0/24"
}

# Create the Internet gateway for the VPC
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.API_VPC.id
}

# Create the Route Table for the VPC
resource "aws_route_table" "api_route" {
  vpc_id = aws_vpc.API_VPC.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }
}

# Create a security group for the EC2 instance
resource "aws_security_group" "instance_sg" {
  name        = "instance_sg"
  description = "Security group for the EC2 instance"

  vpc_id = aws_vpc.API_VPC.id

  # Allow inbound SSH access
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


# Create the ec2 instance itself
resource "aws_instance" "ec2_dashboard_api_host" {
  ami                    = "ami-04b70fa74e45c3917"
  instance_type          = "t2.micro"
  key_name               = "FastAPI2"
  subnet_id              = aws_subnet.main.id
  vpc_security_group_ids = [aws_security_group.instance_sg.id]
}

# Create a simple s3 bucket
resource "aws_s3_bucket" "api-proj-test-bucket" {
  bucket = "api-proj-test-bucket"
}
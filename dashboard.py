from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import boto3

# Creating a variable when calling FastAPI. 
# The templates variable will use the Jinja2Templates and use the dashboard.html for its dir. 
###Note
#The HTML file has to be called dashboad
app = FastAPI()
templates = Jinja2Templates(directory ="/Users/shaikim/Desktop/cloud_projects/AWS")

# The app will send a request to the dashboard.html
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# The app will get the list of instances from us-east-1 
@app.get("/Instances")
def get_Instances():
    ec2 = boto3.client("ec2", region_name= 'us-east-1')
    response = ec2.describe_instances()
    instances = []
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_info = {
                "InstanceId" : instance["InstanceId"],
                "InstanceType" : instance["InstanceType"],
                "State" : instance["State"]["Name"]
            }
            instances.append(instance_info)
    print("Instances:", instances)
    return {"instances": instances}

# The app will get the list of buckets from us-east-1 
@app.get("/Buckets")
def get_Buckets():
    s3 = boto3.client("s3",region_name = 'us-east-1')
    response = s3.list_buckets()
    buckets = []
    for bucket in response['Buckets']:
        bucket_info = {
            "Name" : bucket['Name'],
            "BucketCreationDate" : bucket["CreationDate"]
        }
        buckets.append(bucket_info)
    print("Buckets:", buckets)
    return {"buckets": buckets}

# The app will show the blended cost of the running ec2 instances and s3 buckets
@app.get("/CostExplorer")
def get_cost():
    costs = boto3.client('ce')
    
    response = costs.client.get_cost_and_usage(
        TimePeriod={
            'Start': '2024-04-01',
            'End': '2024-04-30'
        },
        Granularity='Monthly',
        Filter = {
                'CostCategories' : {
                    'Key': 'Service',
                    'Values' : ['AmazonEC2','AmazonS3']
                }      
        },
        Metrics=['BlendedCost'],
    )
    cost_data = response['ResultsByTime'][0]['Total']['BlendedCost']['Amount']
    






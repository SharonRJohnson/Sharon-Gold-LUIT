#Create EC2 instance with (keypair and security) to login from local machine using ssh
import boto3

def create_ec2_instance():
    try:
        print ("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-06e46074ae430fba6",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="Sharon_New_Key"
            
        )  
    except Exception as e:
        print(e)
        
#def describe_ec2_instances():
    try:
        print ("Describing EC2 instance")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        return str(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(e)

#def reboot_ec2_instances():
    try:
        print ("Reboot EC2 instance")
        instance_id = ('i-0573f1d4b96005f2e')
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.reboot_instances(InstanceIds=[instance_id]))  
    except Exception as e:
        print(e) 
        
#def stop_ec2_instances():
    try:
        print ("Stop EC2 instance")
        instance_id = ('i-0573f1d4b96005f2e')
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.stop_instances(InstanceIds=[instance_id]))  
    except Exception as e:
        print(e)

def terminate_ec2_instances():
    try:
        print ("Terminate EC2 instance")
        instance_id = ('i-0573f1d4b96005f2e')
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.terminate_instances(InstanceIds=[instance_id]))  
    except Exception as e:
        print(e)                

#create_ec2_instance()    
#describe_ec2_instance()
#reboot_ec2_instance()
#stop_ec2_instances()
terminate_ec2_instances()        
  
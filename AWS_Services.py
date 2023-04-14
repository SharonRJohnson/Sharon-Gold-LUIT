#Creating a list of AWS Services

#Creating a empty list
services_list = []

#Creating a list of AWS Services 
services_list = ["EC2", "Lambda", "DynamboDB", "S3"]

#Print AWS Services list and list length
print(len(services_list))


#Deleting EC2 and Lambda
services_list.remove("EC2")
services_list.remove("Lambda")
print(services_list)

#Print AWS Service List Update with Length
print(len(services_list))
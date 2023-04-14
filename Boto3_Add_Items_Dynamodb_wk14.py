import boto3
# AWS credentials
aws_access_key_id = 'your keys'
aws_secret_access_key = 'your keys' 
region_name = 'us-east-1' 


# connecting to dynamodb client
dynamodb = boto3.client('dynamodb',
                       aws_access_key_id=aws_access_key_id,
                       aws_secret_access_key=aws_secret_access_key,
                       region_name=region_name)

# function that will add the items to the table
def add_item(brand, flavor):
    table_name = 'FavoriteIceCream'
    try:
       response = dynamodb.put_item(
          TableName=table_name,
          Item={
             'brand': {'S': brand},
             'flavor': {'S': flavor}
          }
       )
       print("Item added:", brand, flavor)
    except Exception as e:  
       print("Error adding item:", e)

add_item("Ben and Jerry", "Chocolate Chip Cookie Dough") 
add_item("Cold Stone Creamery", "Cake Batter")
add_item("Blue Bunny", "Strawberry Shortcake")
add_item("Blue Bell", "Banana Pudding")
add_item("Magnum", "Double Red Velvet")
add_item("Talenti", "Coffe Chocolate Chip")
add_item("Talenti", "Vanilla Caramel Swirl")
add_item("Haagen-dazs", "Strawberry")
add_item("Halo Top", "Oatmeal Cookie")
add_item("Breyers", "Butter Pecan")
add_item("Favorite Ice Cream", "Banana Split")
# the function to scan the table
def scan_table(FavoriteIceCream):
    try:
        response = dynamodb.scan(TableName=FavoriteIceCream)
        items = response['Items']
        print("Table scanned successfully. Items:")
        for item in items:
            print(item)
    except Exception as e:
        print("Error scanning table:", e)


scan_table('FavoriteIceCream')  




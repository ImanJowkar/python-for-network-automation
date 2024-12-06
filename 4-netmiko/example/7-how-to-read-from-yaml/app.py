import yaml

# Define the path to the YAML file
yaml_file_path = 'routers1.yaml'

# Read the YAML file

with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)

print(data)
# # Access the list of dictionaries
routers = data['routers']
print(routers)
# # Print the list of dictionaries
# print(routers)

# # Each router's details can be accessed as a dictionary
# for router in routers:
#     print(f"Host: {router['host']}")
#     print(f"Username: {router['username']}")
#     print(f"Password: {router['password']}")
#     print(f"Port: {router['port']}")
#     print("-------------------------------")

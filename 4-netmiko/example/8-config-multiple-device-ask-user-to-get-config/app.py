import yaml
from netmiko import ConnectHandler

# Define the path to the YAML file
yaml_file_path = 'router1.yaml'

# Read the YAML file
with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)

# Access the list of dictionaries
routers = data['routers']


for router in routers:
    connection = ConnectHandler(**router)
    prompt = connection.find_prompt()

    if '>' in prompt:
        connection.enable()

    if not connection.check_config_mode():
        connection.config_mode()
    print(f"we are currently connected to this router {router['host']}")
    file_name = input("Enter the configuration file name for this router: ")
    res = connection.send_config_from_file(file_name)
    print(res)
    connection.disconnect()
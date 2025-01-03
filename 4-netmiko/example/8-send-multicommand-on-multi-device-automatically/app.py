import yaml
from netmiko import ConnectHandler

# Define the path to the YAML file
yaml_file_path = 'routers.yaml'

# Read the YAML file
with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)

# Access the list of dictionaries
routers = data['routers']


for router in routers:
    config_file_dir = router['config_file_dir']
    del router['config_file_dir']
    print(router)
    connection = ConnectHandler(**router)
    prompt = connection.find_prompt()

    if '>' in prompt:
        connection.enable()

    if not connection.check_config_mode():
        connection.config_mode()
    res = connection.send_config_from_file(config_file_dir)
    print(res)
    connection.disconnect()
    print("-----------------------------------------------------------")
import yaml
from netmiko import ConnectHandler
import threading

# Define the path to the YAML file
yaml_file_path = 'routers.yaml'

# Read the YAML file
with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)

# Access the list of dictionaries
routers = data['routers']


def send_command(router):
    config_file_dir = router['config_file_dir']
    del router['config_file_dir']
    connection = ConnectHandler(**router)
    prompt = connection.find_prompt()
    
    if '>' in prompt:
        connection.enable()
        
    if not connection.check_config_mode():
        connection.config_mode()
    res = connection.send_config_from_file(config_file_dir)        


threads = []
for router in routers:
    th = threading.Thread(target=send_command, args=(router,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()
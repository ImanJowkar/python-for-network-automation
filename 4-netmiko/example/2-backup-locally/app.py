from netmiko import ConnectHandler
from datetime import datetime
import os

# Define the device to connect to
device = {
    'device_type': 'cisco_ios',
    'host': '10.10.200.1',
    'username': 'secret',
    'password': 'secret',
    'secret': 'secret',
}


net_connect = ConnectHandler(**device)
prompt = net_connect.find_prompt()
if '>' in prompt:
    net_connect.enable()




# Get the current date and time for the filename
now = datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M%S")
backup_filename = f"running-config_{timestamp}.cfg"



# Backup running config to local variable
running_config = net_connect.send_command('show running-config')

# Save the running config to a local file
with open(backup_filename, 'w') as backup_file:
    backup_file.write(running_config)

# Close the connection
net_connect.disconnect()
from netmiko import ConnectHandler
from datetime import datetime

# Define the device to connect to
device = {
    'device_type': 'cisco_ios',
    'host': '10.10.200.1',
    'username': 'secret',
    'password': 'secret',
    'secret': 'secret',
}



# Define the FTP server details
ftp_server = '172.16.1.10'
ftp_username = 'admin'
ftp_password = 'admin'

# Connect to the device
net_connect = ConnectHandler(**device)


# Enter enable mode
prompt = net_connect.find_prompt()
if '>' in prompt:
    net_connect.enable()



now = datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M%S")
backup_filename = f"running-config_{timestamp}.cfg"



# Construct the copy command
copy_command = f"copy running-config ftp://{ftp_username}:{ftp_password}@{ftp_server}/{backup_filename}"

# Send the command to the device
output = net_connect.send_command_timing(copy_command)

# Handle the 'Address or name of remote host []?' prompt
if 'Address or name of remote host' in output:
    output += net_connect.send_command_timing('\n')

# Handle the 'Destination filename [backupfile]?' prompt
if 'Destination filename' in output:
    output += net_connect.send_command_timing('\n')

# Print the output
print(output)

# Close the connection
net_connect.disconnect()


print(f"Backup of running-config completed successfully and uploaded to FTP server as {backup_filename}")
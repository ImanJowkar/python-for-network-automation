from netmiko import ConnectHandler
cisco_device = {
       'device_type': 'cisco_ios',     
       'host': '10.10.1.1',
       'username': 'user',
       'password': 'pass',
       'port': 22,             
       'secret': 'enable-pass',      # this is enable password
       'verbose': True        
       }



connection = ConnectHandler(**cisco_device)
prompt = connection.find_prompt()
print(prompt)
if '>' in prompt:
    connection.enable()

output = connection.send_command('sh run')
# output = connection.send_command('sh ip int bri')

print(output)

if not connection.check_config_mode():
    connection.config_mode()

prompt = connection.find_prompt()
print(prompt)

connection.disconnect()
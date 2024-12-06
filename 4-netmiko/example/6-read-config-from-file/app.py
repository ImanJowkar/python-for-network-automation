from netmiko import ConnectHandler
cisco_device = {
       'device_type': 'cisco_ios',
       'host': '10.10.1.5',
       'username': 'user',
       'password': 'pass',
       'port': 22,
       'secret': 'enable-pass',      # this is enable password
       'verbose': True
       }



connection = ConnectHandler(**cisco_device)
prompt = connection.find_prompt()

if '>' in prompt:
    connection.enable()

if not connection.check_config_mode():
    connection.config_mode()




print(connection.send_config_from_file('./cmd'))

connection.disconnect()
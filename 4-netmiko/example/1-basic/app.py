from netmiko import ConnectHandler
cisco_device = {
       'device_type': 'cisco_ios',
       'host': '10.10.200.1',
       'username': 'jack',
       'password': 'jack',
       'port': 22,
       'secret': 'iman',      # this is enable password
       'verbose': True
       }



connection = ConnectHandler(**cisco_device)
prompt = connection.find_prompt()

print(prompt)

if '>' in prompt:
    connection.enable()


prompt = connection.find_prompt()
print(prompt)


if not connection.check_config_mode():
    connection.config_mode()

prompt = connection.find_prompt()
print(prompt)



connection.exit_config_mode()
print(connection.find_prompt())


connection.disconnect()

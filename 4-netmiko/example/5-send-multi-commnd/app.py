from netmiko import ConnectHandler
cisco_device = {
       'device_type': 'cisco_ios',
       'host': '10.10.200.1',
       'username': 'secret',
       'password': 'secret',
       'port': 22,
       'secret': 'secret',      # this is enable password
       'verbose': True
       }



connection = ConnectHandler(**cisco_device)
prompt = connection.find_prompt()

if '>' in prompt:
    connection.enable()



cmd = '''
int loopback 0
ip addr 10.20.30.1 255.255.255.0
no sh
exit

'''



cmd = cmd.split('\n')
print(cmd)
output = connection.send_config_set(cmd)
print(output)
print(connection.find_prompt())
connection.disconnect()


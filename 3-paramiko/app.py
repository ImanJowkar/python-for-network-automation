
import paramiko
import time
import getpass
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
password = getpass.getpass("Please Enter password: ")
router = {'hostname': '192.168.233.100', 'port': '22', 'username': 'iman', 'password': password}

ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
# shell.send('show version\n')
shell.send('show ip int brief\n')
time.sleep(1)

output = shell.recv(10000)
output = output.decode('utf-8')
print(output)

if ssh_client.get_transport().is_active() == True:
    print('Closing the connection')
    ssh_client.close()
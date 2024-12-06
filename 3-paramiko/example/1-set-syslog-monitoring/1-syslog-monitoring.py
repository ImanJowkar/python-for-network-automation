import paramiko
import time
import getpass
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
password = getpass.getpass("Please Enter password: ")

log_server = "192.168.229.100"  # log server
monitoring_server = "172.16.1.1"  # monitorint server
ntp_server = "172.16.2.1"

router1 = {'hostname': '10.10.200.1', 'port': '22', 'username': 'secret', 'password': password}
sw_core = {'hostname': '10.10.200.2', 'port': '22', 'username': 'secret', 'password': password}
sw_acs1 = {'hostname': '10.10.200.3', 'port': '22', 'username': 'secret', 'password': password}
sw_acs2 = {'hostname': '10.10.200.4', 'port': '22', 'username': 'secret', 'password': password}
sw_acs3 = {'hostname': '10.10.200.5', 'port': '22', 'username': 'secret', 'password': password}
routers = [router1, sw_core, sw_acs1, sw_acs2, sw_acs3]

cmd = f'logging host {log_server} transport tcp port 514 session-id hostname\n'
for router in routers:
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

    shell = ssh_client.invoke_shell()
    shell.send('terminal length 0\n')

    shell.send('conf t \n')

    shell.send(cmd)



    shell.send("ip access-list standard snmp-acl\n")
    shell.send(f'permit {monitoring_server}\n')
    shell.send('exit \n')
    shell.send("snmp-server community iman ro snmp-acl\n")
    shell.send('ntp server {ntp_server}\n')

    time.sleep(2)

    output = shell.recv(10000)
    output = output.decode('utf-8')

    if ssh_client.get_transport().is_active() == True:
        print('Closing the connection')
        ssh_client.close()
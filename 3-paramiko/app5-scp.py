import paramiko
from scp import SCPClient

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='10.20.30.1', port='22', username='iman', password='iman',
                       look_for_keys=False, allow_agent=False)


scp = SCPClient(ssh_client.get_transport())


# copy  file
scp.put('file.txt', '/tmp')

scp.close()



# copy directory 
scp.put('dire', recursive = True, remote='/tmp')

scp.close()

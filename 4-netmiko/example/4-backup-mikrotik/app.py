from netmiko import ConnectHandler
mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host':   '192.168.229.163',
    'username': 'admin',
    'password': 'admin',
    'port' : 22          # optional, defaults to 22
}


mikrotik_connect=ConnectHandler(**mikrotik)
backup = mikrotik_connect.send_command('export',cmd_verify=False)
with open('backup.rsc', '+a') as f:
    f.write(backup)


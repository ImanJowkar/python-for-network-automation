from datetime import datetime
from customparamiko import customparamiko
import threading

def backup(device):
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
    h = datetime.now().hour
    m = datetime.now().minute
    ftp_user = "admin"
    ftp_pass = "admin"
    ftp_host = "172.16.1.10"
    client = customparamiko.connect(**device)
    shell = customparamiko.get_shell(client)
    customparamiko.send_command(shell, 'terminal length 0\n')

    backup_filename = f"{device['server_ip']}_{year}_{month}_{day}_{h}_{m}.txt"
    customparamiko.send_command(shell, f'copy running-config ftp://{ftp_user}:{ftp_pass}@{ftp_host}/{backup_filename}.cfg\n\n\n',timout=4)
    #customparamiko.send_command(shell, '\n'}


router1 = {'server_ip': '10.10.200.1', 'server_port': '22', 'user': 'secret', 'passwd': 'secret'}
sw_core = {'server_ip': '10.10.200.2', 'server_port': '22', 'user': 'secret', 'passwd': 'secret'}
sw_acs1 = {'server_ip': '10.10.200.3', 'server_port': '22', 'user': 'secret', 'passwd': 'secret'}
sw_acs2 = {'server_ip': '10.10.200.4', 'server_port': '22', 'user': 'secret', 'passwd': 'secret'}
sw_acs3 = {'server_ip': '10.10.200.5', 'server_port': '22', 'user': 'secret', 'passwd': 'secret'}

devices = [router1, sw_core, sw_acs1, sw_acs2, sw_acs3]

threads = []
for device in devices:
    th = threading.Thread(target=backup, args=(device,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()
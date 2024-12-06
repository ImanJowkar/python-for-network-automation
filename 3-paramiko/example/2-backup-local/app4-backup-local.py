from datetime import datetime
from customparamiko import customparamiko
import threading

def backup(device):
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day

    client = customparamiko.connect(**device)
    shell = customparamiko.get_shell(client)
    customparamiko.send_command(shell, 'terminal length 0\n')
    customparamiko.send_command(shell, "conf t")
    customparamiko.send_command(shell, "do sh run", 5)

    output = customparamiko.show(shell)
    output_list = output.splitlines()
    output_list = output_list[12:-1]
    # print(output_list)

    output = '\n'.join(output_list)
    # print(output)


    output_file_name = f"{device['server_ip']}_{year}_{month}_{day}.txt"



    with open(output_file_name, 'w') as f:
        f.write(output)



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
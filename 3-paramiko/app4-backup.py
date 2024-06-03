from datetime import datetime
from customparamiko import customparamiko
import threading

def backup(router):
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day

    client = customparamiko.connect(**router1)
    shell = customparamiko.get_shell(client)
    customparamiko.send_command(shell, 'terminal length 0\n')
    customparamiko.send_command(shell, "conf t")
    customparamiko.send_command(shell, "do sh run", 5)

    output = customparamiko.show(shell)
    output_list = output.splitlines()
    output_list = output_list[12:-1]
    print(output_list)

    output = '\n'.join(output_list)
    print(output)


    output_file_name = f"{router1['server_ip']}_{year}_{month}_{day}.txt"



    with open(output_file_name, 'w') as f:
        f.write(output)





router1 = {'server_ip': '10.20.30.1', 'server_port': '22', 'user': 'iman', 'passwd': 'iman'}
router2 = {'server_ip': '10.20.30.1', 'server_port': '22', 'user': 'iman', 'passwd': 'iman'}
router3 = {'server_ip': '10.20.30.1', 'server_port': '22', 'user': 'iman', 'passwd': 'iman'}



routers = [router1, router2, router3]

threads = []
for router in routers:
    th = threading.Thread(target=backup, args=(router,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()   

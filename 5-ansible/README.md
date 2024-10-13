# Ansible for network automation

![img](img/1.png)

```
sudo apt install python3-venv

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


ansible --version

sudo apt install sshpass

```

### add ssh config 
```
vim .ssh/config

Host *
    KexAlgorithms +diffie-hellman-group-exchange-sha1
    HostkeyAlgorithms +ssh-rsa
    Ciphers aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc



# run ansible command

ansible --list-hosts all
ansible routers_cisco -m raw -a "show ip int bri" -u iman -k

# run a playbook
ansible-playbook playbook1.yaml -u iman -k

ansible-playbook playbook2.yaml -u iman -k



```
![img](img/2.png)


```
ansible-playbook playbook3.yaml -u iman -k

```

## R1

```

int fa 0/0
no sh
ip address dhcp


ip domain-name iman.local
crypto key generate rsa modulus 2048
ip ssh version 2


username iman privilege 15 secret iman
line vty 0 2
login local
transport input ssh


```



## R2

```


int fa 0/0
no sh
ip address dhcp


ip domain-name iman.local
crypto key generate rsa modulus 2048
ip ssh version 2


username iman privilege 15 secret iman
line vty 0 2
login local
transport input ssh

```

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
vim ~/.ssh/config

Host *
    KexAlgorithms +diffie-hellman-group-exchange-sha1
    HostkeyAlgorithms +ssh-rsa
    Ciphers aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc,aes128-ctr,aes192-ctr,aes256-ctr


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




# ansible vault
ansible-vault create vault.yaml

# add password and sensetive data to this file like below
--------------------------------------
router1_become_pass: pass
router1_ssh_pass: pass

router2_become_pass: pass
router2_become_pass: pass
-----------------------------------------


ansible-vault view vault.yaml # veiw the vault data
ansible-vault rekey vault.yaml # change the vault password
ansible-vault edit vault.yaml # edit the vault file


ansible-playbook playbook3.yaml --ask-vault-pass -e@./vault.yaml

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

# Whole Project


```

# Config

### R4
```

hostname R4

int eth 4/1
no sh
ip addr 192.168.229.50 255.255.255.0

ip route 0.0.0.0 0.0.0.0 192.168.229.2


interface eth 4/0
no sh

interface eth 4/0.10
encapsulation dot1Q 10
ip addr 10.10.10.1 255.255.255.0

interface eth 4/0.20
encapsulation dot1Q 20
ip addr 10.10.20.1 255.255.255.0

interface eth 4/0.200
encapsulation dot1Q 200
ip addr 10.10.200.1 255.255.255.0




ip domain-name iman.test
crypto key generate rsa modulus 2048
ip ssh version 2
username iman privilege 15 secret iman

line vty 0 2
transport input ssh
login local 

```



### SW-Core
```
hostname SW-Core-2


interface range ethernet 0/0-3
switchport trunk encapsulation dot1q
switchport mode trunk


vlan 10,20,200
exit

int vlan 200
ip addr 10.10.200.2 255.255.255.0
no sh



ip route 0.0.0.0 0.0.0.0 10.10.200.1



ip domain-name iman.test
crypto key generate rsa modulus 2048
ip ssh version 2
username iman privilege 15 secret iman

line vty 0 2
transport input ssh
login local 

```


### SW-acs-3
```

hostname SW-acs-3


interface range ethernet 0/0
switchport trunk encapsulation dot1q
switchport mode trunk


vlan 10,20,200
exit

int vlan 200
ip addr 10.10.200.3 255.255.255.0
no sh



ip route 0.0.0.0 0.0.0.0 10.10.200.1



ip domain-name iman.test
crypto key generate rsa modulus 2048
ip ssh version 2
username iman privilege 15 secret iman

line vty 0 2
transport input ssh
login local 
```

### SW-acs-4
```

hostname SW-acs-4


interface range ethernet 0/0
switchport trunk encapsulation dot1q
switchport mode trunk


vlan 10,20,200
exit

int vlan 200
ip addr 10.10.200.4 255.255.255.0
no sh



ip route 0.0.0.0 0.0.0.0 10.10.200.1


ip domain-name iman.test
crypto key generate rsa modulus 2048
ip ssh version 2
username iman privilege 15 secret iman

line vty 0 2
transport input ssh
login local 



```


### SW-acs-5
```


hostname SW-acs-5


interface range ethernet 0/0
switchport trunk encapsulation dot1q
switchport mode trunk


vlan 10,20,200
exit

int vlan 200
ip addr 10.10.200.5 255.255.255.0
no sh



ip route 0.0.0.0 0.0.0.0 10.10.200.1



ip domain-name iman.test
crypto key generate rsa modulus 2048
ip ssh version 2
username iman privilege 15 secret iman

line vty 0 2
transport input ssh
login local 


```

# inventory
```
[SW-acs]
SW-acs-3 ansible_host=10.10.200.3 ansible_user=iman ansible_become_pass=iman ansible_ssh_pass=iman
SW-acs-4 ansible_host=10.10.200.4 ansible_user=iman ansible_become_pass=iman ansible_ssh_pass=iman
SW-acs-5 ansible_host=10.10.200.5 ansible_user=iman ansible_become_pass=iman ansible_ssh_pass=iman



[SW-core]
SW-Core-2 ansible_host=10.10.200.2 ansible_user=iman ansible_become_pass=iman ansible_ssh_pass=iman


[Edge-Router]
R4 ansible_host=10.10.200.1 ansible_user=iman ansible_become_pass=iman ansible_ssh_pass=iman

```

sh version | inc uptime


logging on

logging host 192.168.229.100 transport tcp port 514 session-id hostname



nmap -sn 10.10.200.0/24

1.3.6.1.2.1.1.5.0


snmpwalk -v 2c -c test 10.10.200.3 1.3.6.1.2.1.1.5.0








```
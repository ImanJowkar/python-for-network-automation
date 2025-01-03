# Ansible for Network Engineering


first of all add below config to `~/.ssh/config` file
```

vim ~/.ssh/config

Host *
    KexAlgorithms +diffie-hellman-group-exchange-sha1
    HostkeyAlgorithms +ssh-rsa
    Ciphers aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc,aes128-ctr,aes192-ctr,aes256-ctr

```

#### Install Preqs.
```
sudo apt install python3-venv

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


ansible --version

sudo apt install sshpass

```

#### Enable ssh on device 

```

ip domain-name iman.local
crypto key generate rsa modulus 2048
ip ssh version 2


username iman privilege 15 secret iman
line vty 0 2
login local
transport input ssh


```

### Enable password-less authentication in cisco device:

```
# cisco terminal only accept 256 character in single line


ssh-keygen


fold -b -w 64 ~/.ssh/id_rsa.pub



username iman
ip ssh pubkey-chain
username iman
key-string


! paste here





and change the below config in ~/.ssh/config

Host *
    KexAlgorithms +diffie-hellman-group-exchange-sha1
    HostkeyAlgorithms +ssh-rsa
    Ciphers aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc,aes128-ctr,aes192-ctr,aes256-ctr
    PubkeyAcceptedKeyTypes +ssh-rsa



```


#### Add-Hoc command

```
ansible-inventory --list








```

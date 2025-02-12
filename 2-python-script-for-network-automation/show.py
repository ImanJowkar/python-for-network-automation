from telnetlib import Telnet

print("This program only works in user exec mode. Please enter commands that can be used in this mode. Thanks!")
cmd = input('Enter the Command : ')
username = input("Enter the username: ")
password = input("Enter the password: ")
address = input("Enter the address of the remote device: ")
tel=Telnet(address)
tel.write(username.encode('ascii') + b'\n')
tel.write(password.encode('ascii') + b'\n')

tel.write(b'terminal length 0\n')
tel.write(cmd.encode('ascii') + b'\n')
tel.write(b'exit\n')
print(tel.read_all().decode('ascii'))
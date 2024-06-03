from customparamiko import customparamiko

client = customparamiko.connect('10.20.30.2', '22', 'ubuntu', 'ubuntu')
shell = customparamiko.get_shell(client)

customparamiko.send_command(shell, "cat /etc/passwd")
customparamiko.send_command(shell, "sudo apt update")
customparamiko.send_command(shell, "ubuntu", timout=2)


output = customparamiko.show(shell)
print(output)
from customparamiko import customparamiko

client = customparamiko.connect('10.20.30.1', '22', 'iman', 'iman')
shell = customparamiko.get_shell(client)

customparamiko.send_command(shell, "conf t")
customparamiko.send_command(shell, "do  sh ip int bri")

output = customparamiko.show(shell)
print(output)
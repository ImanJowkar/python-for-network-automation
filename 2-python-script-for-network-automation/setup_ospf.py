import telnetlib

def configure_ospf(ip, username, password, router_id, area, networks):
    try:
        # Connect to the router
        tn = telnetlib.Telnet(ip)

        # Login
        tn.write(username.encode('ascii') + b"\n")
        tn.write(password.encode('ascii') + b"\n")


        # Enter global configuration mode
        tn.write(b"configure terminal\n")

        # Configure OSPF
        tn.write(f"router ospf 1\n".encode('ascii'))
        tn.write(f"router-id {router_id}\n".encode('ascii'))

        for network, wildcard in networks:
            tn.write(f"network {network} {wildcard} area {area}\n".encode('ascii'))

        # Exit configuration mode
        tn.write(b"end\n")
        tn.write(b"write memory\n")
        tn.write(b"exit\n")

        # Print router output
        output = tn.read_all().decode('ascii')
        print(output)

        print(f"OSPF configured successfully on {ip}")

    except Exception as e:
        print(f"Failed to configure OSPF on {ip}: {e}")

device_ip = input("Enter the IP address of the router: ")
username = input("Enter your username: ")
password = input("Enter your password: ")
router_id = input("Enter the OSPF Router ID (e.g., 1.1.1.1): ")
area = input("Enter the OSPF area (e.g., 0): ")

networks = []
while True:
    net = input("Enter network to advertise (e.g., 192.168.1.0), or press Enter to finish: ")
    if not net:
        break
    wildcard = input(f"Enter wildcard mask for {net} (e.g., 0.0.0.255): ")
    networks.append((net, wildcard))
    print(networks)

configure_ospf(device_ip, username, password, router_id, area, networks)

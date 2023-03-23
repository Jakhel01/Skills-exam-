from netmiko import ConnectHandler

# Define the device parameters
device = {
    "device_type": "cisco_ios",
    "ip": "172.20.100.72",
}

# Connect to the device
with ConnectHandler(**device) as net_connect:
    # Task 1a: show IP interface brief
    print("### show ip interface brief ###")
    output = net_connect.send_command("show ip interface brief")
    print(output)

    # Task 1b: show IP route
    print("### show ip route ###")
    output = net_connect.send_command("show ip route")
    print(output)

    # Task 2: create loopback interface lo15
    config_commands = [
        "interface loopback 15",
        "ip address 15.16.17.18 255.255.255.0",
        "no shutdown"
    ]
    output = net_connect.send_config_set(config_commands)
    print("### creating loopback interface lo15 ###")
    print(output)

    # Task 3: create default static route
    config_commands = [
        "ip route 0.0.0.0 0.0.0.0 loopback 15"
    ]
    output = net_connect.send_config_set(config_commands)
    print("### creating default static route ###")
    print(output)

    # Task 4a: show IP interface brief
    print("### show ip interface brief ###")
    output = net_connect.send_command("show ip interface brief")
    print(output)

    # Task 4b: show IP route
    print("### show ip route ###")
    output = net_connect.send_command("show ip route")
    print(output)

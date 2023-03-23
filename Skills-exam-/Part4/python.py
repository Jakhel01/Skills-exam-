import requests


router = "172.20.100.77"  



ifc_config = {
    "ietf-interfaces:interface": {
        "name": "lo14",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ipv6": {
            "address": [
                {
                    "ip": "2001:db8:acad:14::14",
                    "prefix-length": 64
                }
            ]
        }
    }
}

# Send RESTCONF request to create loopback interface
response = requests.post(f"https://{router}/restconf/data/ietf-interfaces:interfaces",
                         auth=(username, password),
                         json=ifc_config, verify=False)

# Print response status code and content
print(f"Status code: {response.status_code}")
print(f"Response content: {response.content}")

# Send RESTCONF request to retrieve loopback interface configuration
response = requests.get(f"https://{router}/restconf/data/ietf-interfaces:interfaces/interface=lo14",
                        auth=(username, password),
                        verify=False)

# Print response status code and content
print(f"Status code: {response.status_code}")
print(f"Response content: {response.content}")

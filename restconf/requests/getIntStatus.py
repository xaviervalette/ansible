# Using python request library for REST operations
from requests.auth import HTTPBasicAuth
import requests
import os
import xmltodict

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Set up device info
username=os.environ["CSR1_SSH_USER"]
password=os.environ["CSR1_SSH_PASS"]
port=os.environ["CSR1_RESTCONF_PORT"]
host=os.environ["CSR1_HOST"]
device_params={"name":"iosxe"}

headers = {
    'Accept': 'application/yang-data+xml',
    'Content-Type': 'application/yang-data+xml',
}

response = requests.get(
    f'https://{host}:{port}/restconf/data/ietf-interfaces:interfaces-state/',
    auth=HTTPBasicAuth(username, password),
    headers=headers,
    verify=False)

# Print out device capabilities.
print(response.text)

cDict = xmltodict.parse(response.text)

print(cDict)
for interface in cDict["interfaces-state"]["interface"]:
    print (f'{interface["name"]} : {interface["oper-status"]}')

    if interface["oper-status"] == "down":
        response = requests.get(
        f'https://{host}:{port}/restconf/data/ietf-interfaces:interfaces/interface={interface["name"]}',
        auth=HTTPBasicAuth(username, password),
        headers=headers,
        verify=False)
        with open(f'{host}_{interface["name"]}.xml', 'w') as f:
            f.write(response.text)
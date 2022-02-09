# Using python request library for REST operations
from requests.auth import HTTPBasicAuth
import requests
import json
import os
# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# Set up device info
username=os.environ["CSR1_USER"]
password=os.environ["CSR1_PASSWORD"]
port=os.environ["CSR1_PORT_NETCONF"]
host=os.environ["CSR1_HOST"]

headers = {
    'Accept': 'application/yang-data+xml',
    'Content-Type': 'application/yang-data+xml',
}

response = requests.get(
    f"https://"+host+":"+port+"/restconf/data/ietf-interfaces:interfaces",
    auth=HTTPBasicAuth(username, password),
    headers=headers,
    verify=False)

# Print out device capabilities.
print(response.text)

with open("%s.xml" % host, 'w') as f:
    f.write(response.text)
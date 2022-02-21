from ncclient import manager
import os
from dotenv import load_dotenv, find_dotenv
import xmltodict

load_dotenv(find_dotenv())

# Set up device info
username=os.environ["CSR1_SSH_USER"]
password=os.environ["CSR1_SSH_PASS"]
port=os.environ["CSR1_NETCONF_PORT"]
host=os.environ["CSR1_HOST"]
device_params={"name":"iosxe"}

"""
Choose and and apply a YANG data model: Native, OpenConfig, IETF
"""
interfacesStateFilter = """ 
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"> 
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    </interfaces-state>
</filter>
"""

"""
Retrieves the operationnal status (up/down) of all devices interfaces
"""
with manager.connect(   host=host, 
                        port=port, 
                        username=username, 
                        password=password, 
                        hostkey_verify=False, 
                        device_params=device_params
) as m:
    c = m.get(interfacesStateFilter).data_xml

cDict = xmltodict.parse(c)

for interface in cDict["data"]["interfaces-state"]["interface"]:
    print (f'{interface["name"]} : {interface["oper-status"]}')
    
    """
    Backup the down's interfaces configuration
    """
    if interface["oper-status"] == "down":
        interfacesFilter = f""" 
        <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"> 
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                    <name>{interface["name"]}</name>
                </interface>
            </interfaces>
        </filter>
        """
        with manager.connect(   host=host, 
            port=port, 
            username=username, 
            password=password, 
            hostkey_verify=False, 
            device_params=device_params
        ) as m:
            data=m.get(interfacesFilter).data_xml

        with open(f'{host}_{interface["name"]}.xml', 'w') as f:
            f.write(data)
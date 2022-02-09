from ncclient import manager
import os
import json

# Set up device info
username=os.environ["CSR1_USER"]
password=os.environ["CSR1_PASSWORD"]
port=os.environ["CSR1_PORT_NETCONF"]
host=os.environ["CSR1_HOST"]
device_params={"name":"iosxe"}

netconf_filter = """ <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"> <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"></interfaces> </filter> """

with manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False, device_params=device_params) as m:
    c = m.get_config('running', netconf_filter).data_xml
    with open("%s_int.xml" % host, 'w') as f:
        f.write(c)
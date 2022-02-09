from ncclient import manager
import os

# Set up device info
username=os.environ["CSR1_USER"]
password=os.environ["CSR1_PASSWORD"]
port=os.environ["CSR1_PORT_NETCONF"]
host=os.environ["CSR1_HOST"]
device_params={"name":"iosxe"}

with manager.connect(host=host, port=830, username=username, password=password, hostkey_verify=False, device_params=device_params) as m:
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % host, 'w') as f:
        f.write(c)
# Run playbook
## Command
```console
devnet@devnet:~/Ansible$ ansible-playbook enableNetconf.yml -i inventory -v
```

## Expected output
```console
Using /etc/ansible/ansible.cfg as config file

PLAY [enable netconf-yang on CSR] *************************************************************************************

TASK [Gathering Facts] ************************************************************************************************
[WARNING]: Ignoring timeout(10) for ansible.legacy.ios_facts
ok: [csr]

TASK [show commands] **************************************************************************************************
ok: [csr] => {"changed": false, "stdout": ["netconf-yang: disabled\nnetconf-yang ssh port: 830\nnetconf-yang candidate-datastore: disabled"], "stdout_lines": [["netconf-yang: disabled", "netconf-yang ssh port: 830", "netconf-yang candidate-datastore: disabled"]]}

TASK [configuration commands] *****************************************************************************************
[WARNING]: To ensure idempotency and correct diff the input configuration lines should be similar to how they appear
if present in the running configuration on device
changed: [csr] => {"banners": {}, "changed": true, "commands": ["netconf-yang"], "updates": ["netconf-yang"]}

TASK [show commands] **************************************************************************************************
ok: [csr] => {"changed": false, "stdout": ["netconf-yang: enabled\nnetconf-yang ssh port: 830\nnetconf-yang candidate-datastore: disabled"], "stdout_lines": [["netconf-yang: enabled", "netconf-yang ssh port: 830", "netconf-yang candidate-datastore: disabled"]]}

PLAY RECAP ************************************************************************************************************
csr                        : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```

# Get Cisco router capabilities
## Command
```console
devnet@devnet:~/Ansible$ ssh -p 830 -s devnet@192.168.1.125 netconf
```
## Expected output
```console
<?xml version="1.0" encoding="UTF-8"?>
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<capabilities>
<capability>urn:ietf:params:netconf:base:1.0</capability>
<capability>urn:ietf:params:netconf:base:1.1</capability>
<capability>urn:ietf:params:netconf:capability:writable-running:1.0</capability>
<capability>urn:ietf:params:netconf:capability:rollback-on-error:1.0</capability>
--- OMITTED OUTPUT ---
```


# Install Ansible core

sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible

# Install Cisco IOS collection

ansible-galaxy collection install cisco.ios

# Install python SSHv2 client

pip install paramiko
# **Ansible Inventory File Guide**

The Ansible inventory file is a key component in defining and organizing the hosts (servers) that you want to manage. This document explains the structure, variables, and advanced arrangements for the inventory file to support scalable infrastructure.

---

## **1. What is an Ansible Inventory File?**
The inventory file lists all the hosts and groups of hosts that Ansible will manage. It can be a simple static file or a dynamic one that queries external systems.

Default location: `/etc/ansible/hosts`

### Supported Formats:
- **INI** (default, text-based)
- **YAML** (preferred for complex setups)
- **Dynamic Inventory** (using plugins or scripts)

---

## **2. Static Inventory File**

### **Basic Example (INI Format)**
```ini
[webservers]
web1.example.com
web2.example.com

[dbservers]
db1.example.com ansible_host=192.168.1.10 ansible_user=admin ansible_port=22
```

### **Host Variables**
Host-specific variables can be defined inline or in a separate file.
```ini
[webservers]
web1.example.com ansible_user=ubuntu
web2.example.com ansible_user=root
```

---

## **3. Grouping Hosts**

### **Group Variables**
Define variables for all hosts in a group using `group_vars/` directory or inline.
```ini
[all:vars]
ansible_user=deploy
ansible_ssh_private_key_file=~/.ssh/id_rsa

[webservers]
web1.example.com
web2.example.com

[dbservers]
db1.example.com
db2.example.com
```

OR:

```plaintext
group_vars/
├── all.yml
├── webservers.yml
└── dbservers.yml
```

#### Example: `group_vars/webservers.yml`
```yaml
nginx_port: 80
```

---

## **4. Advanced Inventory Structure**

### **Child Groups**
Groups can be nested for better organization.
```ini
[webservers]
web1.example.com
web2.example.com

[databases]
db1.example.com
db2.example.com

[production:children]
webservers
databases
```

### **Host-Specific Variables**
Override variables for a specific host.
```ini
[databases]
db1.example.com ansible_host=192.168.1.10 db_type=primary
db2.example.com ansible_host=192.168.1.11 db_type=replica
```

---

## **5. YAML Inventory File**

YAML offers a more readable and structured way to define inventories.

```yaml
all:
  hosts:
    web1.example.com:
      ansible_user: ubuntu
      ansible_port: 22
    db1.example.com:
      ansible_user: root
      ansible_host: 192.168.1.10
  children:
    webservers:
      hosts:
        web1.example.com:
        web2.example.com:
    databases:
      hosts:
        db1.example.com:
        db2.example.com:
```

---

## **6. Dynamic Inventory**

Dynamic inventory scripts or plugins fetch host information from external sources like cloud providers.

### **Example: AWS Dynamic Inventory**
1. Install the required plugin:
   ```bash
   pip install boto3 botocore
   ```
2. Configure a dynamic inventory file (`aws_ec2.yml`):
   ```yaml
   plugin: amazon.aws.ec2
   regions:
     - us-east-1
   filters:
     tag:Environment: production
   keyed_groups:
     - key: tags.Name
       prefix: instance_
   ```

3. Test the inventory:
   ```bash
   ansible-inventory -i aws_ec2.yml --list
   ```

---

## **7. Best Practices for Inventory Files**

### a. Use Directory Structure:
Organize your inventory into directories for clarity and scalability.
```plaintext
inventory/
├── production/
│   ├── hosts.yml
│   └── group_vars/
│       ├── all.yml
│       ├── webservers.yml
│       └── databases.yml
├── staging/
│   ├── hosts.yml
│   └── group_vars/
│       ├── all.yml
│       ├── webservers.yml
│       └── databases.yml
```

### b. Use Dynamic Inventory for Cloud Environments:
Switch to dynamic plugins or scripts for highly dynamic setups like AWS, Azure, or Kubernetes.

### c. Separate Secrets:
Store sensitive information in `ansible-vault` encrypted files.

---

## **8. Example: Large-Scale Inventory**

### INI Format:
```ini
[all:vars]
ansible_user=deploy
ansible_ssh_private_key_file=~/.ssh/id_rsa

[datacenter1:children]
webservers
databases

[webservers]
web1.dc1.example.com
web2.dc1.example.com

[datacenter2:children]
webservers
databases

[webservers]
web1.dc2.example.com
web2.dc2.example.com
```

### YAML Format:
```yaml
all:
  children:
    datacenter1:
      children:
        webservers:
          hosts:
            web1.dc1.example.com:
            web2.dc1.example.com:
        databases:
          hosts:
            db1.dc1.example.com:
            db2.dc1.example.com:
    datacenter2:
      children:
        webservers:
          hosts:
            web1.dc2.example.com:
            web2.dc2.example.com:
        databases:
          hosts:
            db1.dc2.example.com:
            db2.dc2.example.com:
```

---

## **9. Troubleshooting Inventory Issues**

- Use `ansible-inventory` to validate your inventory:
  ```bash
  ansible-inventory -i inventory/ --list
  ```
- Test connection to all hosts:
  ```bash
  ansible all -m ping -i inventory/
  ```
- Enable verbose logging to debug errors:
  ```bash
  ansible-playbook -i inventory/ playbook.yml -vvv
  ```

---

For detailed documentation, visit [Ansible Inventory Documentation](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html).

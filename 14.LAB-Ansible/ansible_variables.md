# **Ansible Variables**

Variables in Ansible are fundamental building blocks for creating dynamic, reusable, and scalable automation tasks. This guide provides an in-depth overview of Ansible variables, their use cases, and best practices for implementation.

---

## **What Are Ansible Variables?**

Ansible variables are placeholders that store dynamic values such as usernames, IP addresses, configuration settings, and more. They allow playbooks to adapt to different environments, making automation flexible and reusable.

---

## **Declaring Variables**

### **1. In Playbooks**
Variables can be defined directly in playbooks under the `vars` section:
```yaml
- name: Example Playbook with Variables
  hosts: localhost
  vars:
    server_name: example.com
    server_port: 8080
  tasks:
    - name: Print server details
      debug:
        msg: "Server {{ server_name }} is running on port {{ server_port }}"
```

### **2. In Inventory Files**
Variables can be assigned to specific hosts or groups in the inventory:
```ini
[web_servers]
server1 ansible_host=192.168.1.10 server_port=80
server2 ansible_host=192.168.1.11 server_port=8080
```

### **3. In Variable Files**
Variables can be stored in external YAML files for better organization:
```yaml
# vars.yml
db_user: admin
db_password: secret
```
Playbook usage:
```yaml
- name: Example with External Variables
  hosts: localhost
  vars_files:
    - vars.yml
  tasks:
    - name: Print database details
      debug:
        msg: "DB User: {{ db_user }}"
```

---

## **Variable Types**

### **1. Simple Variables**
```yaml
username: admin
server_ip: 192.168.1.10
```

### **2. Lists**
```yaml
users:
  - alice
  - bob
  - charlie
```
Accessing list elements:
```yaml
- name: Print first user
  debug:
    msg: "First user is {{ users[0] }}"
```

### **3. Dictionaries**
```yaml
web_config:
  domain: example.com
  port: 80
```
Accessing dictionary keys:
```yaml
- name: Print web domain
  debug:
    msg: "Web domain is {{ web_config.domain }}"
```

---

## **Accessing Variables**

To reference variables, use the double curly braces syntax: `{{ variable_name }}`. This can be used in tasks, templates, and more:
```yaml
- name: Display a variable
  debug:
    msg: "Hello, {{ user_name }}"
```

---

## **Variable Precedence**

Ansible variables have a **precedence hierarchy**, where the source closest to execution takes priority. The order is:

1. Role default variables.
2. Inventory variables (host_vars and group_vars).
3. Playbook variables (vars or vars_files).
4. Extra variables (`-e` in the CLI).

For example:
```bash
ansible-playbook playbook.yml -e "server_port=9090"
```

---

## **Best Practices**

### **1. Use Descriptive Names**
Always use meaningful names for variables to improve readability and maintainability:
```yaml
app_version: 1.0.0
db_host: localhost
```

### **2. Use Defaults for Undefined Variables**
Handle undefined variables using the `default` filter:
```yaml
- name: Use default value
  debug:
    msg: "Server port is {{ server_port | default(8080) }}"
```

### **3. Organize Variables**
Structure your variables using `group_vars` and `host_vars` directories:
```bash
inventory/
  group_vars/
    web_servers.yml
    db_servers.yml
  host_vars/
    server1.yml
    server2.yml
```

### **4. Encrypt Sensitive Variables**
Secure sensitive data (e.g., passwords) with **Ansible Vault**:
```bash
ansible-vault encrypt vars.yml
ansible-vault decrypt vars.yml
```
Use encrypted variables in playbooks seamlessly.

---

## **Advanced Concepts**

### **1. Conditional Variables**
Conditionally define variables using `when` statements:
```yaml
- name: Define variable conditionally
  set_fact:
    environment: production
  when: inventory_hostname == "server1"
```

### **2. Registered Variables**
Capture the output of a task into a variable:
```yaml
- name: Capture command output
  command: whoami
  register: user_info

- name: Display the captured output
  debug:
    msg: "Current user: {{ user_info.stdout }}"
```

### **3. Using Variables in Templates**
Templates allow dynamic content generation using variables. Example `template.j2`:
```html
Welcome to {{ app_name }}!
```
Playbook usage:
```yaml
- name: Generate template file
  template:
    src: template.j2
    dest: /tmp/output.html
  vars:
    app_name: MyApp
```

---

## **Debugging Variables**

Use the `debug` module to inspect variables during playbook execution:
```yaml
- name: Print all available variables
  debug:
    var: hostvars[inventory_hostname]
```

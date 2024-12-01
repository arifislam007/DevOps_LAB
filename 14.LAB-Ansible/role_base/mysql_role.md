# Ansible Role for Apache 
### **Step 1: Role Directory Structure**

Create the `apache` role using `ansible-galaxy`:
```bash
ansible-galaxy init apache
```

---

### **Step 2: Define the Role Content**

#### **1. `tasks/main.yml`** (Tasks to install and configure Apache)
```yaml
---
- name: Install Apache HTTP server
  yum:
    name: httpd
    state: present

- name: Copy custom virtual host configuration
  template:
    src: vhost.conf.j2
    dest: /etc/httpd/conf.d/mywebsite.conf
  notify: Restart Apache

- name: Ensure Apache service is enabled and started
  service:
    name: httpd
    state: started
    enabled: true
```

---

#### **2. `handlers/main.yml`** (Restart Apache service when configuration changes)
```yaml
---
- name: Restart Apache
  service:
    name: httpd
    state: restarted
```

---

#### **3. `templates/vhost.conf.j2`** (Custom Virtual Host Configuration)
```jinja
<VirtualHost *:80>
    ServerAdmin webmaster@{{ apache_server_name }}
    DocumentRoot {{ apache_document_root }}
    ServerName {{ apache_server_name }}
    ErrorLog /var/log/httpd/{{ apache_server_name }}-error.log
    CustomLog /var/log/httpd/{{ apache_server_name }}-access.log combined
</VirtualHost>
```

---

#### **4. `defaults/main.yml`** (Default Variables for Customization)
```yaml
---
apache_server_name: localhost
apache_document_root: /var/www/html
```

---

#### **5. `files/index.html`** (Static HTML File for Testing)
```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to {{ apache_server_name }}</title>
</head>
<body>
    <h1>It works!</h1>
</body>
</html>
```

---

### **Step 3: Use the Role in a Playbook**

Create a playbook `site.yml` to apply this role.

#### **`site.yml`**
```yaml
---
- name: Configure Apache Web Server
  hosts: web_servers
  become: true
  roles:
    - apache
```

---

### **Step 4: Inventory File**

Create an inventory file `inventory` with your server details.

#### **`inventory`**
```ini
[web_servers]
web1.example.com
```

---

### **Step 5: Run the Playbook**

Run the playbook to configure Apache:
```bash
ansible-playbook -i inventory site.yml
```

---

### **Customization**
- Update the `defaults/main.yml` variables to match your server's configuration.
- Replace `web1.example.com` in the inventory with your server's IP or hostname.

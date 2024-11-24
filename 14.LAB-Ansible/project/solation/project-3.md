### **Project: LAMP Stack Deployment with Ansible**

This project focuses on automating the deployment of a **LAMP (Linux, Apache, MySQL, PHP)** stack, which is a foundational setup for hosting web applications. It introduces modular playbooks using roles, handlers, and templates.

---

### **Objective**
1. Install and configure Apache as the web server.
2. Install and configure MySQL as the database server.
3. Install PHP and ensure it works with Apache.
4. Use modular roles for better organization.

---

### **Requirements**
- Ansible installed on the control node.
- Target servers with SSH access and Python installed.
- Basic understanding of Ansible roles and templates.

---

### **Steps**

#### **1. Prepare the Inventory File**
Create `inventory.ini` with server details:
```ini
[webservers]
192.168.1.10 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa

[dbservers]
192.168.1.11 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
```

---

#### **2. Create Directory Structure**
Use `ansible-galaxy` to create roles for modular organization:
```bash
mkdir lamp_stack && cd lamp_stack
ansible-galaxy init roles/apache
ansible-galaxy init roles/mysql
ansible-galaxy init roles/php
```

Directory structure:
```
lamp_stack/
├── inventory.ini
├── playbook.yml
└── roles/
    ├── apache/
    ├── mysql/
    └── php/
```

---

#### **3. Configure Apache Role**
Edit `roles/apache/tasks/main.yml`:
```yaml
---
- name: Install Apache
  apt:
    name: apache2
    state: present
  notify:
    - Restart Apache

- name: Copy the website configuration file
  template:
    src: vhost.conf.j2
    dest: /etc/apache2/sites-available/000-default.conf
  notify:
    - Restart Apache

- name: Enable mod_rewrite
  command: a2enmod rewrite
  notify:
    - Restart Apache
```

Create a template for the virtual host: `roles/apache/templates/vhost.conf.j2`:
```apache
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html

    <Directory /var/www/html>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

Define a handler for Apache in `roles/apache/handlers/main.yml`:
```yaml
---
- name: Restart Apache
  service:
    name: apache2
    state: restarted
```

---

#### **4. Configure MySQL Role**
Edit `roles/mysql/tasks/main.yml`:
```yaml
---
- name: Install MySQL server
  apt:
    name: mysql-server
    state: present

- name: Secure MySQL installation
  command: mysql_secure_installation
  args:
    creates: /etc/mysql/.secure
```

Optionally, set root password or configure a database in `roles/mysql/tasks/main.yml`:
```yaml
- name: Set MySQL root password
  mysql_user:
    name: root
    password: "securepassword"
    host: localhost
    priv: "*.*:ALL,GRANT"
```

---

#### **5. Configure PHP Role**
Edit `roles/php/tasks/main.yml`:
```yaml
---
- name: Install PHP and extensions
  apt:
    name: "{{ item }}"
    state: present
  loop:
    - php
    - libapache2-mod-php
    - php-mysql

- name: Create a PHP test page
  copy:
    dest: /var/www/html/info.php
    content: "<?php phpinfo(); ?>"
```

---

#### **6. Create the Main Playbook**
Create `playbook.yml` to include roles:
```yaml
---
- name: Deploy LAMP Stack
  hosts: all
  become: true
  roles:
    - apache
    - mysql
    - php
```

---

#### **7. Run the Playbook**
Execute the playbook:
```bash
ansible-playbook -i inventory.ini playbook.yml
```

---

#### **8. Verify the Deployment**
1. **Apache:** Open `http://<webserver-ip>` in your browser. You should see the default Apache page.
2. **PHP:** Visit `http://<webserver-ip>/info.php` to confirm PHP is installed and working.
3. **MySQL:** Log in to MySQL:
   ```bash
   mysql -u root -p
   ```

---

### **Enhancements**

#### **1. Add SSL Support**
Use `certbot` to automate SSL configuration:
```yaml
- name: Install Certbot for SSL
  apt:
    name: python3-certbot-apache
    state: present

- name: Obtain and install SSL certificate
  command: certbot --apache -d example.com --non-interactive --agree-tos -m admin@example.com
```

---

#### **2. Automate Firewall Rules**
Add tasks for `ufw` in `roles/apache/tasks/main.yml`:
```yaml
- name: Allow HTTP and HTTPS traffic
  ufw:
    rule: allow
    port: "{{ item }}"
    proto: tcp
  loop:
    - 80
    - 443
```

---

#### **3. Database Initialization**
Automatically create a database and a user in `roles/mysql/tasks/main.yml`:
```yaml
- name: Create a database
  mysql_db:
    name: myapp
    state: present

- name: Create a database user
  mysql_user:
    name: appuser
    password: "apppassword"
    priv: "myapp.*:ALL"
    state: present
```

---

### **Learning Outcomes**
- Modularize playbooks using roles for better scalability.
- Use templates to dynamically generate configuration files.
- Automate service restarts with handlers.
- Deploy a fully functional web application stack.

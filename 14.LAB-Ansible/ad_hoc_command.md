### **Common Ad-Hoc Commands in Ansible**

Ansible's **ad-hoc commands** are one-off tasks that you can execute without writing a playbook. They are quick and effective for testing or performing simple operations on managed nodes. Below are some common ad-hoc commands organized by functionality:

---

### **1. Ping Nodes**
Check connectivity between the control node and managed hosts:
```bash
ansible all -m ping
```

---

### **2. Gather Facts**
Retrieve information (facts) about the managed nodes:
```bash
ansible all -m setup
```

Gather specific facts (e.g., hostname):
```bash
ansible all -m setup -a "filter=ansible_hostname"
```

---

### **3. Manage Files and Directories**
- **Create a Directory**:
  ```bash
  ansible all -m file -a "path=/tmp/test_directory state=directory"
  ```
- **Create a File**:
  ```bash
  ansible all -m file -a "path=/tmp/test_file state=touch"
  ```
- **Delete a File/Directory**:
  ```bash
  ansible all -m file -a "path=/tmp/test_file state=absent"
  ```

---

### **4. Copy Files**
Copy a file from the control node to the managed nodes:
```bash
ansible all -m copy -a "src=/path/to/local/file dest=/path/to/remote/file"
```

---

### **5. Install or Remove Packages**
- **Install a Package** (e.g., `nginx`):
  ```bash
  ansible all -m apt -a "name=nginx state=present" --become
  ```
  (For CentOS/Red Hat, replace `apt` with `yum` or `dnf`.)

- **Remove a Package**:
  ```bash
  ansible all -m apt -a "name=nginx state=absent" --become
  ```

---

### **6. Manage Services**
- **Start a Service** (e.g., `nginx`):
  ```bash
  ansible all -m service -a "name=nginx state=started" --become
  ```
- **Stop a Service**:
  ```bash
  ansible all -m service -a "name=nginx state=stopped" --become
  ```
- **Restart a Service**:
  ```bash
  ansible all -m service -a "name=nginx state=restarted" --become
  ```

---

### **7. Run Shell Commands**
Execute shell commands on managed nodes:
```bash
ansible all -m shell -a "uptime"
```

Run a command with a specific user:
```bash
ansible all -m shell -a "df -h" --become --become-user=username
```

---

### **8. Manage Users**
- **Add a User**:
  ```bash
  ansible all -m user -a "name=johndoe state=present" --become
  ```
- **Remove a User**:
  ```bash
  ansible all -m user -a "name=johndoe state=absent" --become
  ```

---

### **9. Manage Groups**
- **Create a Group**:
  ```bash
  ansible all -m group -a "name=devops state=present" --become
  ```
- **Delete a Group**:
  ```bash
  ansible all -m group -a "name=devops state=absent" --become
  ```

---

### **10. Manage Cron Jobs**
- **Add a Cron Job**:
  ```bash
  ansible all -m cron -a "name='Backup Job' minute=0 hour=3 job='/usr/bin/backup.sh'" --become
  ```
- **Remove a Cron Job**:
  ```bash
  ansible all -m cron -a "name='Backup Job' state=absent" --become
  ```

---

### **11. Reboot a Node**
Reboot all managed nodes:
```bash
ansible all -m reboot --become
```

---

### **12. Check Disk Usage**
Get disk usage information:
```bash
ansible all -m shell -a "df -h"
```

---

### **13. Check System Uptime**
Check how long the systems have been running:
```bash
ansible all -m shell -a "uptime"
```

---

### **14. Manage Hosts File**
Add an entry to the `/etc/hosts` file:
```bash
ansible all -m lineinfile -a "path=/etc/hosts line='192.168.1.10 myserver.local' state=present" --become
```

---

### **15. Manage Environment Variables**
Add an environment variable to `/etc/environment`:
```bash
ansible all -m lineinfile -a "path=/etc/environment line='APP_ENV=production' state=present" --become
```

---

### **16. Manage Archives**
- **Extract a tar.gz Archive**:
  ```bash
  ansible all -m unarchive -a "src=/path/to/archive.tar.gz dest=/opt/ extract=yes" --become
  ```

---

### **17. Manage Firewalls**
- **Add a Firewall Rule**:
  ```bash
  ansible all -m ufw -a "rule=allow port=80 proto=tcp" --become
  ```
- **Enable Firewall**:
  ```bash
  ansible all -m ufw -a "state=enabled" --become
  ```

---

### **18. Manage Docker Containers**
- **Run a Docker Container**:
  ```bash
  ansible all -m docker_container -a "name=my_container image=nginx state=started" --become
  ```
- **Stop a Docker Container**:
  ```bash
  ansible all -m docker_container -a "name=my_container state=stopped" --become
  ```

---

### **19. Synchronize Directories**
Sync directories between control and managed nodes:
```bash
ansible all -m synchronize -a "src=/local/path dest=/remote/path" --become
```

---

### **20. Debug Variables**
Output the value of a specific variable:
```bash
ansible all -m debug -a "msg='Hello, Ansible!'"
```

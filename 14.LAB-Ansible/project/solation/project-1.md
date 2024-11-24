### **Project: Automating Package Installation with Ansible**

This project is ideal for beginners and focuses on automating the installation of common system packages across multiple servers. It will help you learn basic Ansible concepts, including inventory, playbooks, and modules.

---

### **Objective**
Create an Ansible playbook that:
1. Installs essential packages (e.g., `curl`, `git`, `htop`) on target systems.
2. Ensures idempotency—packages are installed only if they are missing.

---

### **Requirements**
- Ansible installed on your control node (laptop or server).
- Target servers with SSH access and Python installed.
- A basic understanding of YAML syntax.

---

### **Steps**

#### **1. Create an Inventory File**
An inventory file lists the servers you want to manage.

Create a file named `inventory.ini`:
```ini
[webservers]
192.168.1.10 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
192.168.1.11 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa

[dbservers]
192.168.1.12 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
```

**Explanation:**
- `[webservers]` and `[dbservers]` are host groups.
- Specify the SSH user and private key for each server.

---

#### **2. Write the Playbook**
Create a file named `install_packages.yml`:
```yaml
- name: Install essential packages on servers
  hosts: all
  become: true  # Run tasks with sudo privileges
  vars:
    common_packages:
      - curl
      - git
      - htop
  tasks:
    - name: Update the package cache
      apt:
        update_cache: yes
      when: ansible_os_family == "Debian"

    - name: Ensure required packages are installed (Debian-based)
      apt:
        name: "{{ item }}"
        state: present
      loop: "{{ common_packages }}"
      when: ansible_os_family == "Debian"

    - name: Ensure required packages are installed (RHEL-based)
      yum:
        name: "{{ item }}"
        state: present
      loop: "{{ common_packages }}"
      when: ansible_os_family == "RedHat"

    - name: Print a debug message
      debug:
        msg: "Package installation complete on {{ inventory_hostname }}"
```

**Explanation:**
- **`hosts: all`**: Targets all servers in the inventory.
- **`become: true`**: Elevates privileges using `sudo`.
- **`vars:`**: Defines reusable variables like `common_packages`.
- **`when:`**: Adds conditional execution based on the OS family.
- **`loop:`**: Iterates over a list of packages.

---

#### **3. Test the Playbook**
Run the playbook with the following command:
```bash
ansible-playbook -i inventory.ini install_packages.yml
```

**Expected Output:**
- The playbook will connect to each server in the inventory.
- It will update the package cache and install the listed packages.
- If a package is already installed, Ansible will skip it.

---

#### **4. Verify the Results**
Log into one of the target servers and check:
1. The package cache is updated:
   ```bash
   sudo apt update  # For Debian/Ubuntu
   sudo yum update  # For RHEL/CentOS
   ```
2. The packages are installed:
   ```bash
   dpkg -l | grep curl  # For Debian/Ubuntu
   rpm -q curl          # For RHEL/CentOS
   ```

---

### **Enhancements**
1. **Add More Packages:**
   Update `common_packages` to include additional tools like `vim`, `wget`, or `tree`.

2. **Log Output:**
   Use the `lineinfile` module to log the installed packages to a file on the target server.

3. **Error Handling:**
   Add a `rescue` block to handle package installation failures:
   ```yaml
   - block:
       - name: Install package
         apt:
           name: "{{ item }}"
           state: present
         loop: "{{ common_packages }}"
     rescue:
       - name: Log failure
         debug:
           msg: "Failed to install {{ item }} on {{ inventory_hostname }}"
   ```

4. **Dynamic Package Lists:**
   Use group-specific variables in `group_vars/webservers.yml`:
   ```yaml
   common_packages:
     - nginx
     - curl
   ```

---

### **Learning Outcomes**
- Understand the basics of Ansible inventory and playbooks.
- Use modules like `apt` and `yum` for package management.
- Apply loops and conditionals for cross-platform automation.
- Validate idempotency in Ansible tasks.

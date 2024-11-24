### **Project: User and SSH Key Management with Ansible**

This project focuses on automating the creation of user accounts and managing their SSH keys across multiple servers. It introduces loops, variables, and the use of the `user` and `authorized_key` modules in Ansible.

---

### **Objective**
1. Create and manage user accounts on multiple servers.
2. Add SSH public keys to the created users' `authorized_keys` files.
3. Ensure idempotency—users and keys should not be duplicated.

---

### **Requirements**
- Ansible installed on the control node.
- Target servers accessible via SSH.
- A basic inventory file listing the servers.

---

### **Steps**

#### **1. Prepare Inventory File**
Create a file named `inventory.ini`:
```ini
[webservers]
192.168.1.10 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
192.168.1.11 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa

[dbservers]
192.168.1.12 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
```

---

#### **2. Define SSH Keys**
Create a file named `user_vars.yml` to define users and their SSH keys:
```yaml
users:
  - name: deploy
    ssh_key: "ssh-rsa AAAAB3...your-public-key... user@example.com"
  - name: admin
    ssh_key: "ssh-rsa AAAAB3...another-public-key... admin@example.com"
```

---

#### **3. Write the Playbook**
Create a playbook named `manage_users.yml`:
```yaml
- name: Manage users and SSH keys
  hosts: all
  become: true  # Run tasks as a privileged user
  vars_files:
    - user_vars.yml
  tasks:
    - name: Create user accounts
      user:
        name: "{{ item.name }}"
        state: present
        shell: /bin/bash
      loop: "{{ users }}"

    - name: Add SSH public keys for users
      authorized_key:
        user: "{{ item.name }}"
        key: "{{ item.ssh_key }}"
        state: present
      loop: "{{ users }}"

    - name: Verify users and keys setup
      debug:
        msg: "User {{ item.name }} is set up with SSH key."
      loop: "{{ users }}"
```

**Explanation:**
- **`vars_files:`**: Loads external variables (usernames and keys).
- **`loop:`**: Iterates over the `users` list to perform tasks for each user.
- **Modules Used:**
  - **`user`**: Creates user accounts.
  - **`authorized_key`**: Manages SSH keys.

---

#### **4. Run the Playbook**
Execute the playbook using the command:
```bash
ansible-playbook -i inventory.ini manage_users.yml
```

**Expected Output:**
- The playbook creates the users on all target servers.
- Each user's SSH key is added to their `~/.ssh/authorized_keys` file.
- A confirmation message is displayed for each user.

---

#### **5. Verify Results**
1. Log into one of the target servers:
   ```bash
   ssh ubuntu@192.168.1.10
   ```

2. Check that the users exist:
   ```bash
   cat /etc/passwd | grep deploy
   ```

3. Verify the SSH key is added:
   ```bash
   cat /home/deploy/.ssh/authorized_keys
   ```

---

### **Enhancements**

#### **1. Configure Passwords**
Set a password for each user (optional):
```yaml
- name: Create user accounts with passwords
  user:
    name: "{{ item.name }}"
    password: "{{ item.password | password_hash('sha512') }}"
  loop: "{{ users }}"
```
Update `user_vars.yml` to include passwords:
```yaml
users:
  - name: deploy
    ssh_key: "ssh-rsa AAAAB3...your-public-key... user@example.com"
    password: "your-secure-password"
```

---

#### **2. Add User Groups**
Assign users to specific groups:
```yaml
- name: Add users to groups
  user:
    name: "{{ item.name }}"
    groups: "sudo"
    append: true
  loop: "{{ users }}"
```

---

#### **3. Remove Inactive Users**
Clean up users that are no longer required:
```yaml
- name: Remove inactive users
  user:
    name: "{{ item.name }}"
    state: absent
  loop:
    - name: old_user
```

---

#### **4. Handle Errors with Blocks**
Use error handling for failed tasks:
```yaml
- block:
    - name: Create user
      user:
        name: "{{ item.name }}"
    - name: Add SSH key
      authorized_key:
        user: "{{ item.name }}"
        key: "{{ item.ssh_key }}"
  rescue:
    - name: Log failure
      debug:
        msg: "Failed to create or configure user {{ item.name }}"
  loop: "{{ users }}"
```

---

#### **5. Integrate Ansible Vault**
Secure sensitive information like SSH keys or passwords:
```bash
ansible-vault encrypt user_vars.yml
```

---

### **Learning Outcomes**
- Manage users and SSH keys programmatically.
- Use loops and external variable files effectively.
- Enhance security by automating SSH key deployment.
- Debug playbooks and handle errors gracefully.

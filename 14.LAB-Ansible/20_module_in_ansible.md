# 20 commonly used Ansible modules


### **File and Directory Management**
1. **`file`**  
   - Manages files and directories (create, delete, set permissions).
   - Example: Create a directory with specific permissions.
     ```yaml
     - name: Create a directory
       file:
         path: /path/to/directory
         state: directory
         mode: '0755'
     ```

2. **`copy`**  
   - Copies files from the control node to managed nodes.
   - Example: Copy a configuration file.
     ```yaml
     - name: Copy a file
       copy:
         src: /local/path/file.conf
         dest: /remote/path/file.conf
     ```

3. **`template`**  
   - Processes Jinja2 templates and transfers them to the target.
   - Example: Use a template for configuration.
     ```yaml
     - name: Deploy configuration template
       template:
         src: nginx.conf.j2
         dest: /etc/nginx/nginx.conf
     ```

---

### **Package Management**
4. **`apt`** *(Debian/Ubuntu)*  
   - Manages packages on Debian-based systems.
   - Example: Install Apache.
     ```yaml
     - name: Install Apache
       apt:
         name: apache2
         state: present
     ```

5. **`yum`** *(CentOS/Red Hat)*  
   - Manages packages on Red Hat-based systems.
   - Example: Install Nginx.
     ```yaml
     - name: Install Nginx
       yum:
         name: nginx
         state: latest
     ```

6. **`dnf`** *(CentOS 8+)*  
   - Successor to `yum` for managing packages on newer Red Hat-based systems.

---

### **Service Management**
7. **`service`**  
   - Manages services (start, stop, enable, restart).
   - Example: Restart a service.
     ```yaml
     - name: Restart Apache
       service:
         name: apache2
         state: restarted
     ```

8. **`systemd`**  
   - Manages systemd services.
   - Example: Start and enable a service.
     ```yaml
     - name: Start and enable Docker
       systemd:
         name: docker
         state: started
         enabled: true
     ```

---

### **User and Group Management**
9. **`user`**  
   - Manages user accounts.
   - Example: Create a user.
     ```yaml
     - name: Add a user
       user:
         name: deploy
         state: present
     ```

10. **`group`**  
    - Manages groups on the system.
    - Example: Add a user to a group.
      ```yaml
      - name: Add user to group
        user:
          name: deploy
          groups: sudo
          append: yes
      ```

---

### **Networking**
11. **`firewalld`** *(Red Hat)*  
    - Configures and manages `firewalld`.
    - Example: Open port 80.
      ```yaml
      - name: Allow HTTP traffic
        firewalld:
          port: 80/tcp
          permanent: true
          state: enabled
      ```

12. **`ufw`** *(Ubuntu)*  
    - Configures Uncomplicated Firewall (UFW).
    - Example: Allow SSH traffic.
      ```yaml
      - name: Allow SSH
        ufw:
          rule: allow
          port: 22
          proto: tcp
      ```

13. **`lineinfile`**  
    - Ensures a specific line is present in a file.
    - Example: Add a DNS server entry.
      ```yaml
      - name: Add DNS entry
        lineinfile:
          path: /etc/resolv.conf
          line: "nameserver 8.8.8.8"
      ```

---

### **Task Execution and Shell**
14. **`command`**  
    - Executes a command on the target node.
    - Example: Run a basic command.
      ```yaml
      - name: List directory contents
        command: ls /home
      ```

15. **`shell`**  
    - Executes a shell command on the target node.
    - Example: Run a script.
      ```yaml
      - name: Run a script
        shell: ./setup.sh
      ```

16. **`raw`**  
    - Executes a raw command without using the Ansible module system.
    - Example: Use raw for basic SSH commands.
      ```yaml
      - name: Run a raw command
        raw: apt-get update
      ```

---

### **Cloud and Containers**
17. **`docker_container`**  
    - Manages Docker containers.
    - Example: Deploy a container.
      ```yaml
      - name: Start an Nginx container
        docker_container:
          name: nginx
          image: nginx
          state: started
      ```

18. **`ec2`** *(AWS)*  
    - Provisions EC2 instances on AWS.
    - Example: Launch an EC2 instance.
      ```yaml
      - name: Launch EC2 instance
        ec2:
          key_name: my_key
          instance_type: t2.micro
          image: ami-123456
          wait: yes
      ```

---

### **Utilities**
19. **`debug`**  
    - Prints debugging messages during playbook execution.
    - Example: Print variable values.
      ```yaml
      - name: Show variable value
        debug:
          msg: "The value of my_var is {{ my_var }}"
      ```

20. **`set_fact`**  
    - Defines or overrides variables during runtime.
    - Example: Set a dynamic variable.
      ```yaml
      - name: Set a custom fact
        set_fact:
          custom_var: "value"
      ```

### **Project: Deploying Docker Containers with Ansible**

This project focuses on automating the installation of Docker and deploying a containerized application using Ansible. It covers installing Docker, managing containers, and ensuring idempotency.

---

### **Objective**
1. Install Docker on target servers.
2. Deploy and manage containerized applications (e.g., an Nginx web server).
3. Automate Docker container updates and configuration.

---

### **Requirements**
- Ansible installed on the control node.
- Target servers accessible via SSH.
- Basic knowledge of Docker concepts.

---

### **Steps**

#### **1. Prepare Inventory File**
Create `inventory.ini` to define your target servers:
```ini
[dockerservers]
192.168.1.20 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
```

---

#### **2. Create the Directory Structure**
Set up a project directory:
```bash
mkdir docker_deployment && cd docker_deployment
```

Directory structure:
```
docker_deployment/
├── inventory.ini
├── playbook.yml
└── roles/
    └── docker/
        ├── tasks/
        │   ├── main.yml
        │   ├── install_docker.yml
        │   ├── deploy_container.yml
        ├── defaults/
        │   └── main.yml
```

---

#### **3. Configure the Docker Role**

##### **3.1 Install Docker**
Edit `roles/docker/tasks/install_docker.yml`:
```yaml
---
- name: Update apt package index
  apt:
    update_cache: yes

- name: Install Docker dependencies
  apt:
    name:
      - apt-transport-https
      - ca-certificates
      - curl
      - software-properties-common
    state: present

- name: Add Docker’s official GPG key
  apt_key:
    url: https://download.docker.com/linux/ubuntu/gpg
    state: present

- name: Add Docker repository
  apt_repository:
    repo: "deb [arch=amd64] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} stable"
    state: present

- name: Install Docker CE
  apt:
    name: docker-ce
    state: present

- name: Ensure Docker service is running
  service:
    name: docker
    state: started
    enabled: true
```

##### **3.2 Deploy Containers**
Edit `roles/docker/tasks/deploy_container.yml`:
```yaml
---
- name: Pull the latest Nginx image
  docker_image:
    name: nginx
    source: pull

- name: Deploy an Nginx container
  docker_container:
    name: nginx
    image: nginx
    ports:
      - "80:80"
    state: started
    restart_policy: always
```

##### **3.3 Main Task File**
Edit `roles/docker/tasks/main.yml`:
```yaml
---
- import_tasks: install_docker.yml
- import_tasks: deploy_container.yml
```

---

#### **4. Define Default Variables**
Edit `roles/docker/defaults/main.yml`:
```yaml
---
docker_version: "latest"
nginx_container_name: "nginx"
```

---

#### **5. Create the Main Playbook**
Create `playbook.yml` to include the Docker role:
```yaml
---
- name: Deploy Docker and containers
  hosts: dockerservers
  become: true
  roles:
    - docker
```

---

#### **6. Run the Playbook**
Execute the playbook:
```bash
ansible-playbook -i inventory.ini playbook.yml
```

**Expected Output:**
- Docker is installed on the target servers.
- An Nginx container is deployed and accessible via the server's IP on port 80.

---

#### **7. Verify the Deployment**
1. Check Docker is installed:
   ```bash
   ssh ubuntu@192.168.1.20
   docker --version
   ```
2. Verify the Nginx container is running:
   ```bash
   docker ps
   ```
3. Visit `http://192.168.1.20` in your browser to see the default Nginx page.

---

### **Enhancements**

#### **1. Deploy Multiple Containers**
Deploy additional containers by adding tasks to `roles/docker/tasks/deploy_container.yml`:
```yaml
- name: Deploy a MySQL container
  docker_container:
    name: mysql
    image: mysql:5.7
    ports:
      - "3306:3306"
    env:
      MYSQL_ROOT_PASSWORD: "rootpassword"
    state: started
    restart_policy: always
```

---

#### **2. Use Docker Compose**
Deploy complex multi-container applications using Docker Compose:
1. Install Docker Compose:
   ```yaml
   - name: Install Docker Compose
     get_url:
       url: https://github.com/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m`
       dest: /usr/local/bin/docker-compose
       mode: '0755'
   ```
2. Add a `docker-compose.yml` template file for the application.

---

#### **3. Automate Image Updates**
Ensure images are up-to-date using `docker_image`:
```yaml
- name: Update Docker images
  docker_image:
    name: nginx
    source: pull
```

---

### **Learning Outcomes**
- Install and manage Docker with Ansible.
- Automate containerized application deployment.
- Use variables and modular tasks for scalable automation.
- Leverage Ansible's Docker modules for image and container management.

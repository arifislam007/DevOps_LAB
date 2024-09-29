## Kubernetes on Rocky Linux

Here's an Ansible playbook to deploy Kubernetes using **Kubeadm** on Rocky Linux 9 with a 3-node setup (1 master and 2 worker nodes).

### 1. Inventory File

First, create an inventory file defining your nodes.

**`inventory.yml`**:
```yaml
all:
  hosts:
    master:
      ansible_host: 192.168.1.101  # IP address of the master node
    worker1:
      ansible_host: 192.168.1.102  # IP address of the first worker node
    worker2:
      ansible_host: 192.168.1.103  # IP address of the second worker node

  vars:
    ansible_user: your_username    # Replace with your SSH user
    ansible_become: yes
```

### 2. Ansible Playbook

Next, create the playbook to install Kubernetes.

**`kubernetes-deploy.yml`**:
```yaml
---
- name: Deploy Kubernetes cluster using Kubeadm
  hosts: all
  become: yes
  tasks:
    - name: Disable SELinux
      command: setenforce 0
      when: ansible_os_family == "RedHat"

    - name: Ensure SELinux is disabled permanently
      lineinfile:
        path: /etc/sysconfig/selinux
        regexp: '^SELINUX='
        line: 'SELINUX=disabled'

    - name: Disable swap
      command: swapoff -a
      when: ansible_os_family == "RedHat"

    - name: Ensure swap is disabled permanently
      lineinfile:
        path: /etc/fstab
        regexp: '^.*swap'
        state: absent

    - name: Install required packages
      dnf:
        name:
          - curl
          - wget
          - vim
          - git
          - net-tools
        state: present

    - name: Add Kubernetes YUM repository
      yum_repository:
        name: kubernetes
        description: Kubernetes YUM Repository
        baseurl: https://packages.cloud.google.com/yum/doc/yum-key.gpg
        enabled: yes
        gpgcheck: yes
        gpgkey: https://packages.cloud.google.com/yum/doc/yum-key.gpg
        repo_gpgcheck: yes

    - name: Install Kubernetes packages
      dnf:
        name:
          - kubelet
          - kubeadm
          - kubectl
        state: latest

    - name: Enable kubelet service
      systemd:
        name: kubelet
        enabled: yes
        state: started

- name: Initialize Kubernetes cluster
  hosts: master
  become: yes
  tasks:
    - name: Initialize Kubernetes using Kubeadm
      command: kubeadm init --pod-network-cidr=192.168.0.0/16
      register: kubeadm_output
      ignore_errors: yes

    - name: Set up kubeconfig for the user
      copy:
        dest: /home/{{ ansible_user }}/.kube/config
        src: /etc/kubernetes/admin.conf
        owner: "{{ ansible_user }}"
        group: "{{ ansible_user }}"
        mode: '0644'
      when: kubeadm_output.rc == 0

    - name: Install Calico network plugin
      command: kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
      when: kubeadm_output.rc == 0

- name: Join worker nodes to the cluster
  hosts: worker1:worker2
  become: yes
  tasks:
    - name: Join the cluster
      command: "{{ hostvars['master']['kubeadm_output'].stdout_lines[-1] }}"
      when: hostvars['master']['kubeadm_output'] is defined
```

### 3. Run the Playbook

To run the playbook, execute the following command from your control node:

```bash
ansible-playbook -i inventory.yml kubernetes-deploy.yml
```

### Explanation

- The playbook performs the following tasks:
  - Disables SELinux and swap.
  - Installs required packages.
  - Sets up the Kubernetes repository and installs **kubelet**, **kubeadm**, and **kubectl**.
  - Initializes the Kubernetes cluster on the master node.
  - Configures `kubectl` for the user.
  - Installs the Calico network plugin.
  - Joins the worker nodes to the cluster using the join command captured during initialization.

### Note

- Make sure to replace `your_username` in the inventory file with your actual SSH user.
- The `pod-network-cidr` is set to `192.168.0.0/16`, which is commonly used with Calico; adjust as needed for other network plugins.
- Ensure you capture the join command output from the master node during initialization if needed for debugging.

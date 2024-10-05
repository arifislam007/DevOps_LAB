bash```
---
- name: Deploy Kubernetes on Rocky Linux 9
  hosts: all
  become: yes
  tasks:
    # COMMON TASKS FOR BOTH MASTER AND WORKERS

    - name: Disable SELinux temporarily
      command: setenforce 0
      when: ansible_os_family == "RedHat"

    - name: Ensure SELinux is disabled permanently
      lineinfile:
        path: /etc/sysconfig/selinux
        regexp: '^SELINUX='
        line: 'SELINUX=disabled'

    - name: Disable swap
      command: swapoff -a

    - name: Ensure swap is disabled permanently
      lineinfile:
        path: /etc/fstab
        regexp: '^.*swap'
        state: absent

    - name: Enable IP forwarding
      sysctl:
        name: net.ipv4.ip_forward
        value: 1
        state: present
        reload: yes

    - name: Install socat package
      dnf:
        name: socat
        state: present

    - name: Install required dependencies for Docker repository
      dnf:
        name:
          - yum-utils
          - device-mapper-persistent-data
          - lvm2
        state: present

    - name: Add Docker repository
      yum_repository:
        name: docker
        description: Docker CE Stable - $basearch
        baseurl: https://download.docker.com/linux/centos/8/$basearch/stable
        gpgcheck: yes
        gpgkey: https://download.docker.com/linux/centos/gpg
        enabled: yes

    - name: Install containerd
      dnf:
        name: containerd
        state: present

    - name: Enable and start containerd
      systemd:
        name: containerd
        enabled: yes
        state: started

    - name: Install required packages
      dnf:
        name:
          - curl
          - wget
          - vim
          - git
          - net-tools
          - iproute-tc
        state: present

    - name: Add Kubernetes YUM repository
      yum_repository:
        name: kubernetes
        description: Kubernetes YUM Repository
        baseurl: https://pkgs.k8s.io/core:/stable:/v1.30/rpm/
        enabled: yes
        gpgcheck: yes
        gpgkey: https://pkgs.k8s.io/core:/stable:/v1.30/rpm/repodata/repomd.xml.key
        repo_gpgcheck: yes

    - name: Install Kubernetes packages
      dnf:
        name:
          - kubelet
          - kubeadm
          - kubectl
        state: latest

    - name: Enable and start kubelet service
      systemd:
        name: kubelet
        enabled: yes
        state: started

    - name: Load required kernel modules
      modprobe:
        name: br_netfilter

    - name: Ensure sysctl parameters for Kubernetes networking
      sysctl:
        name: net.bridge.bridge-nf-call-iptables
        value: 1
        sysctl_set: yes
        state: present

# MASTER NODE TASKS

- name: Initialize Kubernetes on Master
  hosts: master
  become: yes
  tasks:
    - name: Initialize Kubernetes Cluster with Kubeadm
      command: kubeadm init
      register: kubeadm_init
      ignore_errors: yes

    - name: Copy Kubeconfig to the default user
      copy:
        src: /etc/kubernetes/admin.conf
        dest: /home/{{ ansible_user }}/.kube/config
        remote_src: yes
        owner: "{{ ansible_user }}"
        group: "{{ ansible_user }}"
        mode: '0644'
      when: kubeadm_init.rc == 0

    - name: Remove config.toml file
      file:
        path: /etc/containerd/config.toml
        state: absent

    - name: Install Weave Net network plugin
      command: kubectl apply -f https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')
      when: kubeadm_init.rc == 0

    - name: Generate the join command for worker nodes
      command: kubeadm token create --print-join-command
      register: join_command
      when: kubeadm_init.rc == 0

# WORKER NODE TASKS

- name: Join Worker Nodes to the Kubernetes Cluster
  hosts: workers
  become: yes
  tasks:
    - name: Join worker node to the cluster
      command: "{{ hostvars['master']['join_command'].stdout }}"
      ignore_errors: yes

```

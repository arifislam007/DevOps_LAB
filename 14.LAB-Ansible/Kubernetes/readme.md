# Deploy Kubernetes on Rocky Linux 9 using Ansible

This Ansible playbook will deploy a Kubernetes cluster on Rocky Linux 9 with both master and worker nodes. It handles common system configurations, installs necessary dependencies, and initializes the cluster with a master node and one or more workers.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Common Setup for Master and Worker Nodes](#common-setup-for-master-and-worker-nodes)
- [Master Node Setup](#master-node-setup)
- [Worker Node Setup](#worker-node-setup)

## Prerequisites

- Ensure that the `hosts` file is configured properly to group your nodes as `master` and `workers`.
- Ansible must be installed on the control machine.
- Root (sudo) access is required on all target nodes.

## Common Setup for Master and Worker Nodes

The following tasks are run on both master and worker nodes:

```yaml
---
- name: Deploy Kubernetes on Rocky Linux 9
  hosts: all
  become: yes
  tasks:
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
        baseurl: https://download.docker.com/linux/centos/8/$basearch/stable
        gpgcheck: yes
        gpgkey: https://download.docker.com/linux/centos/gpg
        enabled: yes

    - name: Install containerd
      dnf:
        name: containerd
        state: present

    - name: Remove config.toml file
      file:
        path: /etc/containerd/config.toml
        state: absent

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
```

## Master Node Setup

The following tasks are specific to the master node:

```yaml
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

    - name: Install Weave Net network plugin
      command: kubectl apply -f https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')
      when: kubeadm_init.rc == 0

    - name: Generate the join command for worker nodes
      command: kubeadm token create --print-join-command
      register: join_command
      when: kubeadm_init.rc == 0
```

## Worker Node Setup

The following tasks join worker nodes to the Kubernetes cluster:

```yaml
- name: Join Worker Nodes to the Kubernetes Cluster
  hosts: workers
  become: yes
  tasks:
    - name: Join worker node to the cluster
      command: "{{ hostvars['master']['join_command'].stdout }}"
      ignore_errors: yes
```

## How to Use

1. Clone the repository and update the `hosts` file with your inventory.
2. Run the playbook:

   ```bash
   ansible-playbook -i hosts kubernetes-rocky.yml
   ```

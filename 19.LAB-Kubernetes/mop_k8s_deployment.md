Method of Procedure (MOP) for Kubernetes Cluster Provisioning on AlmaLinux 9
Title: Provisioning a 3-Node Kubernetes Cluster (1 Master, 2 Workers) on AlmaLinux 9

Purpose:
To outline the steps required to provision a Kubernetes cluster with 1 master node and 2 worker nodes on AlmaLinux 9, using containerd as the container runtime and Kubernetes version 1.30.

Scope:
This MOP applies to the deployment of a Kubernetes cluster on AlmaLinux 9 servers with the following IPs and hostnames:

Master Node: 192.168.2.250 (hostname: k8s-master)
Worker Node 1: 192.168.2.251 (hostname: worker-node-1)
Worker Node 2: 192.168.2.252 (hostname: worker-node-2)
Prerequisites:

AlmaLinux 9 servers are provisioned and accessible.
SSH access to all servers with root or sudo privileges.
Internet access for downloading Kubernetes binaries and container images.
Firewall rules configured to allow communication between nodes (ports 6443, 2379, 2380, 10250, 10259, 10257, etc.).
Swap disabled on all nodes (swapoff -a and remove swap entries from /etc/fstab).
Unique hostnames and static IPs assigned to all nodes.
Roles and Responsibilities:

DevOps Engineer: Execute the deployment steps.
System Administrator: Configure servers and networking.
QA Engineer: Validate the Kubernetes cluster functionality.
Specifications:
OS: AlmaLinux 9
Container Runtime: containerd
Kubernetes Version: 1.30
Step 1: Prepare All Nodes
Set Hostname:

sudo hostnamectl set-hostname k8s-master   # Run on master node
sudo hostnamectl set-hostname worker-node-1 # Run on worker node 1
sudo hostnamectl set-hostname worker-node-2 # Run on worker node 2
Update System Packages:

sudo dnf update -y
sudo dnf install -y vim git curl wget bash-completion net-tools
Disable Swap:

sudo swapoff -a
sudo sed -i '/swap/d' /etc/fstab
Configure Kernel Parameters for Kubernetes:

cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter

cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
net.bridge.bridge-nf-call-ip6tables = 1
EOF

sudo sysctl --system
Step 2: Install Containerd
Install Dependencies:

sudo dnf install -y yum-utils
Add Docker Repository:

sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
Install Containerd:

sudo dnf install -y containerd.io
Configure Containerd:

containerd config default | sudo tee /etc/containerd/config.toml > /dev/null
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
Restart and Enable Containerd:

sudo systemctl restart containerd
sudo systemctl enable containerd
Step 3: Install Kubernetes Components
Add Kubernetes Repository:

cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.30/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.30/rpm/repodata/repomd.xml.key
EOF
Install Kubernetes Packages:

sudo dnf install -y kubelet kubeadm kubectl
Enable Kubelet:

sudo systemctl enable --now kubelet
Step 4: Initialize Kubernetes Cluster (Master Node Only)
Initialize the Master Node:

sudo kubeadm init --control-plane-endpoint=k8s-master
Set Up Kubeconfig:

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
Deploy Network Plugin (Calico):

kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
Retrieve Join Command:

kubeadm token create --print-join-command
This will output a join command. Copy and use it in the next step.

Step 5: Join Worker Nodes
Run the Join Command on Each Worker Node:

sudo kubeadm join 192.168.2.250:6443 --token <TOKEN> \
    --discovery-token-ca-cert-hash sha256:<HASH>
Verify Node Status (On Master Node):

kubectl get nodes
All nodes should appear in Ready status.

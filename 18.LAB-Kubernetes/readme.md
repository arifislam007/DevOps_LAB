# Kubernetes Overview

## What is Kubernetes?

Kubernetes (commonly referred to as K8s) is an open-source platform designed to automate the deployment, scaling, and management of containerized applications. Originally developed by Google, Kubernetes helps manage containerized applications across a cluster of nodes, providing fault tolerance, load balancing, and scalability for distributed systems.

Key features of Kubernetes include:

- **Automated deployment and scaling**: Manage large numbers of containers and scale them based on resource demand.
- **Self-healing**: Automatically replace and reschedule containers that fail, ensuring high availability.
- **Service discovery and load balancing**: Automatically assign IP addresses to containers and distribute traffic between containers.
- **Storage orchestration**: Automatically mount storage systems like local storage, cloud providers, and network storage.

## Components of Kubernetes

Kubernetes is made up of several components that together manage the infrastructure, ensure the health of the system, and provide the necessary services to the containerized applications. The key components include:

### 1. **Master Node Components**:

- **API Server**: The API server is the front-end of the Kubernetes control plane, providing an interface for interacting with the cluster through REST API calls.
  
- **Etcd**: A distributed key-value store used to store all the data of the Kubernetes cluster, such as configurations, secrets, and state information.
  
- **Scheduler**: Determines which node an unscheduled pod should run on based on resource availability and requirements.
  
- **Controller Manager**: Responsible for running controllers (processes that regulate the state of the cluster), such as Node Controller, Replication Controller, and Endpoints Controller.

### 2. **Worker Node Components**:

- **Kubelet**: An agent that runs on each node, ensuring that the containers are running as expected in the pods. It communicates with the API server to receive tasks and report the status of the nodes.

- **Kube-proxy**: A network proxy that runs on each node and manages network rules, allowing communication between pods, both within and outside of the cluster.

- **Container Runtime**: The software responsible for running containers (e.g., Docker, containerd).

### 3. **Additional Components**:

- **Ingress Controller**: Manages external access to services, usually through HTTP and HTTPS routing.
  
- **Cluster DNS**: Manages DNS records for services, allowing them to be accessed using human-readable domain names.

## Objects of Kubernetes

Kubernetes uses various objects to represent the desired state of the system. These objects are persistent entities in the cluster, each with a well-defined structure. Key Kubernetes objects include:

### 1. **Pod**
The smallest and simplest Kubernetes object, a Pod represents a single instance of a running process in your cluster. It encapsulates one or more containers and shared resources such as storage and network.

### 2. **Service**
A Service is an abstraction that defines a logical set of Pods and a policy to access them. Services allow communication between different components of the application, both within and outside the cluster.

### 3. **Deployment**
A Deployment object provides declarative updates to Pods and ReplicaSets. It's responsible for ensuring that a specified number of Pods are running and updating the Pods when necessary (e.g., rolling updates).

### 4. **ReplicaSet**
The ReplicaSet ensures that a specified number of pod replicas are running at any given time. It's commonly used by Deployments to maintain a stable set of pods.

### 5. **ConfigMap**
A ConfigMap stores configuration data in key-value pairs that can be consumed by containers or injected into Pods as environment variables.

### 6. **Secret**
Similar to ConfigMaps but intended for sensitive data (like passwords, OAuth tokens, etc.). Secrets are stored in an encrypted format.

### 7. **PersistentVolume (PV) & PersistentVolumeClaim (PVC)**
PV represents a storage resource, while PVC is a request for storage by a user. Together, they manage how storage is requested and made available to Pods.

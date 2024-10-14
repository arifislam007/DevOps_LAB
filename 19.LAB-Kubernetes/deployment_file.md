
# NGINX Deployment with Service in Kubernetes
## Overview

In this example:
- We create a **Deployment** to manage the NGINX Pods.
- We expose these Pods using a **Service** of type **NodePort** so that the NGINX server can be accessed from outside the Kubernetes cluster.

## Deployment and Service Explanation

### Deployment

The **Deployment** ensures that the NGINX Pods are always running, with the specified number of replicas. It also provides support for rolling updates and fault tolerance by managing the Pods' lifecycle.

### Service

The **Service** of type **NodePort** will expose the NGINX Pods on a static port across all the nodes in the cluster, allowing external traffic to access the NGINX application.

## Example Deployment Manifest

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3  # Number of NGINX replicas
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest  # NGINX image from Docker Hub
        ports:
        - containerPort: 80
```

### Key Points:
- **replicas**: The number of NGINX instances (Pods) that will be running.
- **image**: The Docker image for NGINX (using the latest version).
- **containerPort**: NGINX is listening on port 80 inside the container.

## Example Service Manifest

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx  # This matches the Deployment label
  ports:
    - protocol: TCP
      port: 80  # Service port
      targetPort: 80  # Container port in the Pod
      nodePort: 30007  # Node port to expose externally
  type: NodePort  # Service type to expose NGINX externally
```

### Key Points:
- **selector**: Matches the Pods that the Service should target based on labels.
- **port**: The port that the Service will listen on.
- **targetPort**: The port that the container is exposing.
- **nodePort**: The port on each node where the service can be accessed externally.
- **type**: `NodePort` allows external traffic to be forwarded to the NGINX Pods.

## How to Apply the Manifests

1. Save the Deployment manifest as `nginx-deployment.yaml`:
   ```bash
   kubectl apply -f nginx-deployment.yaml
   ```

2. Save the Service manifest as `nginx-service.yaml`:
   ```bash
   kubectl apply -f nginx-service.yaml
   ```

3. Once applied, the NGINX web server will be running in the cluster and can be accessed through the node's IP and the specified **NodePort** (in this case, `30007`).

For example, if your node's IP is `192.168.1.100`, you can access NGINX by opening the following URL in your browser:
```
http://192.168.1.100:30007
```

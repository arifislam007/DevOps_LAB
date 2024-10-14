# Nginx Web Server on Kubernetes

This repository contains a simple Kubernetes Pod definition to deploy an Nginx web server using the official Nginx image.

## Pod Definition

The `nginx-pod.yaml` file defines a Pod that runs an Nginx container. Below is a breakdown of the YAML file:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-webserver
  labels:
    app: nginx
spec:
  containers:
  - name: nginx-container
    image: nginx:latest
    ports:
    - containerPort: 80
```

### Key Sections

- **apiVersion:** Specifies the API version (`v1` for core resources like Pod).
- **kind:** Defines the resource type (`Pod`).
- **metadata:**
  - **name:** The name of the Pod (`nginx-webserver`).
  - **labels:** Labels to help identify and group the Pod (`app: nginx`).
- **spec:** The main specification for the Pod, including:
  - **containers:** A list of containers to run in the Pod.
    - **name:** The name of the container (`nginx-container`).
    - **image:** The container image to use (`nginx:latest`).
    - **ports:** The port Nginx will serve on inside the container (`containerPort: 80`).

## How to Apply

To create the Nginx web server Pod, use the following command:

```bash
kubectl apply -f nginx-pod.yaml
```

This will deploy the Pod on your Kubernetes cluster, and you can verify the status using:

```bash
kubectl get pods
```

## Accessing the Web Server

By default, the Nginx container will serve HTTP traffic on port 80. To access the web server:

1. Use `kubectl port-forward` to forward the container port to your local machine:
   ```bash
   kubectl port-forward pod/nginx-webserver 8080:80
   ```

2. Open your browser and navigate to `http://localhost:8080` to see the Nginx welcome page.

## Cleanup

To delete the Pod when you're done, run:

```bash
kubectl delete -f nginx-pod.yaml
```

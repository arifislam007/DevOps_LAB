# Kubernetes Manifest File

This repository contains example Kubernetes manifest files that define the configuration for various Kubernetes resources such as Pods, Deployments, and Services. A **manifest file** in Kubernetes is a YAML or JSON file that describes the desired state of resources in the cluster.

## What is a Manifest File?

A **Kubernetes manifest file** is used to define the configuration of Kubernetes resources, including:
- Pods
- Deployments
- Services
- ConfigMaps
- PersistentVolumes
and more.

The manifest file is written in YAML or JSON format, and it specifies the **desired state** of the resource. Kubernetes uses this file to ensure that the actual state of your cluster matches the desired state described in the manifest.

### Key Components of a Manifest File

1. **apiVersion**:
   - Specifies the version of the Kubernetes API to use.
   - Example: `apiVersion: v1`

2. **kind**:
   - Defines the type of Kubernetes resource (e.g., Pod, Service, Deployment).
   - Example: `kind: Deployment`

3. **metadata**:
   - Contains information like the name and labels for the resource.
   - Example:
     ```yaml
     metadata:
       name: my-app
       labels:
         app: web
     ```

4. **spec**:
   - Defines the desired state of the resource. The content of the spec depends on the resource type.
   - Example for a Pod:
     ```yaml
     spec:
       containers:
       - name: nginx
         image: nginx:latest
         ports:
         - containerPort: 80
     ```

5. **status** (optional):
   - Represents the current state of the resource, which Kubernetes automatically manages. It is not manually defined by users.

## Example of a Manifest File

Here’s an example manifest file that defines a Kubernetes Deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
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
        image: nginx:1.16
        ports:
        - containerPort: 80
```

- **apiVersion:** Specifies the API version for managing Deployments.
- **kind:** Specifies the resource type (`Deployment`).
- **metadata:** Contains the name and labels for the Deployment.
- **spec:** Describes the desired state, including:
  - Number of replicas (3).
  - Container image (`nginx:1.16`).
  - The port the container will expose (80).

## How to Use a Manifest File

1. **Apply the manifest**: Use the following command to apply the manifest to your Kubernetes cluster:
   ```bash
   kubectl apply -f <manifest-file.yaml>
   ```

2. **View the resource**: You can check if the resource is created and running with:
   ```bash
   kubectl get pods
   ```

3. **Delete the resource**: When you are done, you can delete the resource using:
   ```bash
   kubectl delete -f <manifest-file.yaml>
   ```

## Benefits of Manifest Files

- **Declarative Configuration**: Kubernetes uses a declarative approach to manage resources, ensuring the desired state described in the manifest is always maintained.
- **Version Control**: You can store manifest files in Git for version control, making it easier to track and manage changes.
- **Automation**: Manifest files enable automation of deployments through CI/CD pipelines.
- **Scalability**: Kubernetes can automatically scale resources defined in manifest files based on cluster load or manual scaling commands.

# Kubernetes Services, ConfigMaps, and Secrets

## What is a Service?

A **Service** in Kubernetes is an abstraction that defines a logical set of Pods and a policy to access them. It enables communication between different parts of your application and provides a stable endpoint for accessing Pods, regardless of their dynamic lifecycle. Services can be exposed internally or externally, making it easier to connect various application components.

### Key Features of Services:
- Load balancing: Distributes traffic across multiple Pods.
- Stable endpoints: Provides a consistent way to access Pods.
- Service types: ClusterIP, NodePort, LoadBalancer, and ExternalName.

## What is a ConfigMap?

A **ConfigMap** is a Kubernetes object that allows you to store non-sensitive configuration data as key-value pairs. ConfigMaps decouple configuration from application code, making it easier to manage and change configurations without redeploying applications.

### Key Features of ConfigMaps:
- Store configuration data in key-value pairs.
- Inject configuration data into Pods as environment variables or mounted volumes.
- Easily update configurations without redeploying the application.

## What is a Secret?

A **Secret** is a Kubernetes object used to store sensitive information, such as passwords, OAuth tokens, and SSH keys. Secrets are encoded and can be consumed by Pods securely, ensuring that sensitive data is not exposed in the application code or logs.

### Key Features of Secrets:
- Store sensitive information securely.
- Base64 encoded to protect data.
- Can be consumed as environment variables or mounted volumes.

## Use Cases

- **Services** are used when you need to enable communication between different Pods or expose an application to external clients.
- **ConfigMaps** are useful for managing application configurations that can change over time without requiring redeployment.
- **Secrets** are essential for securely managing sensitive information in applications.

## Example Manifests

### Service Manifest Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: ClusterIP
```

### ConfigMap Manifest Example

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-app-config
data:
  APP_MODE: "production"
  LOG_LEVEL: "info"
```

### Secret Manifest Example

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-app-secret
type: Opaque
data:
  username: dXNlcm5hbWU=  # base64 encoded value
  password: cGFzc3dvcmQ=  # base64 encoded value
```

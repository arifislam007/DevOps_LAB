# Grafana SMTP Alerting Setup on Kubernetes

This repository contains all necessary Kubernetes manifests to deploy Grafana with SMTP alerting configured using secrets. Follow the instructions below to set up Grafana with SMTP alert notifications.

## Prerequisites

- A running Kubernetes cluster.
- `kubectl` configured to interact with your Kubernetes cluster.
- SMTP credentials (username, password, and SMTP server) for sending email notifications.

## Step 1: Create a Kubernetes Secret for SMTP Credentials

First, create a Kubernetes secret to securely store your SMTP credentials. This will avoid having SMTP credentials in plain text within the manifest files.

Run the following command:

```bash
kubectl create secret -n monitoring generic notifications-smtp \
  --from-literal=user=<smtp username> \
  --from-literal=password=<smtp password> \
  --from-literal=host=<smtp server:port>
```

This command will create a secret named `notifications-smtp` in the `monitoring` namespace containing the SMTP credentials.

## Step 2: Grafana Deployment Configuration

The Grafana deployment manifest (`deployment.yaml`) is configured to use the created SMTP secret. It enables email notifications and provides the necessary SMTP settings.

Here's the `deployment.yaml` configuration:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: grafana
  namespace: monitoring
spec:
  replicas: 1
  selector:
    matchLabels:
      app: grafana
  template:
    metadata:
      name: grafana
      labels:
        app: grafana
    spec:
      containers:
      - name: grafana
        image: grafana/grafana:latest
        env:
          - name: GF_SMTP_ENABLED
            value: "true"
          - name: GF_SMTP_FROM_ADDRESS
            value: "your_mail_from_address"
          - name: GF_SMTP_FROM_NAME
            value: "Grafana monitoring"
          # Use the secret to define these values
          - name: GF_SMTP_HOST
            valueFrom:
              secretKeyRef:
                name: notifications-smtp
                key: host
          - name: GF_SMTP_PASSWORD
            valueFrom:
              secretKeyRef:
                name: notifications-smtp
                key: password
          - name: GF_SMTP_USER
            valueFrom:
              secretKeyRef:
                name: notifications-smtp
                key: user
        ports:
        - name: grafana
          containerPort: 3000
        resources:
          limits:
            memory: "1Gi"
            cpu: "1000m"
          requests:
            memory: 500M
            cpu: "500m"
        volumeMounts:
          - mountPath: /var/lib/grafana
            name: grafana-storage
          - mountPath: /etc/grafana/provisioning/datasources
            name: grafana-datasources
            readOnly: false
      volumes:
        - name: grafana-storage
          emptyDir: {}
        - name: grafana-datasources
          configMap:
              defaultMode: 420
              name: grafana-datasources
        - name: grafana-config
          configMap:
            name: grafana-smtp-config
```

**Make sure to replace** `your_mail_from_address` with your actual email address that will be used for sending alerts.

## Step 3: Grafana Datasource Configuration

Create a ConfigMap to configure Grafana's datasource (e.g., Prometheus) for monitoring. Here's an example `grafana-datasource-config.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: grafana-datasources
  namespace: monitoring
data:
  prometheus.yaml: |-
    {
        "apiVersion": 1,
        "datasources": [
            {
               "access": "proxy",
               "editable": true,
               "name": "prometheus",
               "orgId": 1,
               "type": "prometheus",
               "url": "http://prometheus-service.monitoring.svc:8080",
               "version": 1
            }
        ]
    }
```

## Step 4: Grafana Service Configuration

Expose Grafana via a Kubernetes service by creating a `service.yaml` file. This will expose Grafana on a NodePort so you can access it externally.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: grafana
  namespace: monitoring
  annotations:
      prometheus.io/scrape: 'true'
      prometheus.io/port:   '3000'
spec:
  selector:
    app: grafana
  type: NodePort
  ports:
    - port: 3000
      targetPort: 3000
      nodePort: 32000
```

## Step 5: Deploy Grafana with All Configs

After creating the necessary files (e.g., `deployment.yaml`, `config-map.yaml`, `grafana-datasource-config.yaml`, and `service.yaml`), apply the resources to your Kubernetes cluster:

```bash
kubectl apply -f grafana-datasource-config.yaml
kubectl apply -f service.yaml
kubectl apply -f deployment.yaml
```

## Step 6: Access Grafana

After deploying, Grafana should be accessible via the NodePort on your Kubernetes node. You can access it using the following URL:

```
http://<node-ip>:32000
```

Log in with the default credentials (username: `admin`, password: `admin`).

## Optional: Clone the Repository

You can also clone this GitHub repository and update the deployment file with your specific details:

```bash
git clone https://github.com/bibinwilson/kubernetes-grafana.git
```

Make the necessary changes and follow the steps to deploy.

## Conclusion

This setup configures Grafana with SMTP for alerting, using Kubernetes secrets to manage sensitive credentials securely. You can now monitor your systems and receive email alerts for various thresholds and conditions.

For further customization or issues, feel free to modify the files or raise an issue on GitHub.

```

This `README.md` file guides users through setting up Grafana with SMTP email alerting in a Kubernetes environment, including steps for creating secrets, configuring Grafana, and deploying everything into the cluster.

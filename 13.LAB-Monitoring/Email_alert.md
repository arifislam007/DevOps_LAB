### First, we create a secret so that we don't have SMTP credentials sat in a random manifest:

```yaml
kubectl create secret -n monitoring generic notifications-smtp --from-literal=user=<smtp username> --from-literal=password=<smtp password> --from-literal=host=<smtp server:port>
```
### This command will create secret like following 
![image](https://github.com/user-attachments/assets/f0aa0521-e45f-41de-91af-882c7e7a985c)


### Now Wirte the deployment file for grafana 
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

- set your mail from the address here

### Now deploy grafana mainfest with all other relevant file like: deployment.yaml, config-map.yaml, datastore.yaml, service.yaml 
Write the following file here:
- grafana-datasource-config.yaml
  
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
               "access":"proxy",
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


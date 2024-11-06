### First, we create a secret so that we don't have SMTP credentials sat in a random manifest:
```yaml
kubectl create secret generic notifications-smtp --from-literal=user=<smtp username> --from-literal=password=<smtp password> --from-literal=host=<smtp server:port>
```
